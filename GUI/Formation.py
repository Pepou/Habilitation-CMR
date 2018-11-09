# -*- coding: utf-8 -*-

"""
Module implementing Formation.
"""

from PyQt4.QtCore import pyqtSlot, pyqtSignal, Qt, QThread, QRunnable, QObject, QThreadPool, QMutex
from PyQt4.QtGui import (QMainWindow, QTableWidgetItem, QTextEdit, 
                            QCheckBox, QStandardItemModel, QBrush, QColor, 
                            QStandardItem, QComboBox)

from .Ui_Formation import Ui_Formation
from Package.AccesBdd import Bdd_Cmr, Insertion_Domaine
import pendulum
import json

class Formation(QMainWindow, Ui_Formation):
    """
    Class documentation goes here.
    """
    #signal
    fermeture_reouverture = pyqtSignal()
    maj = pyqtSignal()
    
    def __init__(self, engine , gui_parent, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle ("Enregistrement d'une formation")
        
        self.engine = engine
        self.dateEdit.setDate(pendulum.now('Europe/Paris'))        
        self.cmr_bdd = Bdd_Cmr(self.engine)
        
        gen_cmr =self.cmr_bdd.recup_cmr_en_activite()
        
        self.remplir_tableau_cmr(next(gen_cmr))
        
#        self.threadpool = QThreadPool()
        
        self.gui_parent = gui_parent
        
        ####Threads
        self.thread_finish = False
#        self.affectation_lancement_threads()
        
        
        init_domaine = Insertion_Domaine(self.engine)
        areas = init_domaine.recuperation_domaine()
#        print(areas)
        
        self.model = QStandardItemModel((len(areas)+1), 1)# 5 rows, 1 col
        
        firstItem = QStandardItem("---- Select domaine(s) ----")
        firstItem.setBackground(QBrush(QColor(200, 200, 200)))
        firstItem.setSelectable(False)
        self.model.setItem(0, 0, firstItem)
        
        for i,area in enumerate(areas):
            item = QStandardItem(area)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
            self.model.setItem(i+1, 0, item)
            
        self.comboBox_domaine.setModel(self.model)
        

        self.gui_parent.formation_a_modifier.connect(self.reaffectation_formation)
#        
#    def affectation_lancement_threads(self):
#        """"met en place les threads et les lance"""
        
#        bdd_thread = Gestion_BDD_Thread(self.cmr_bdd )
#        bdd_thread.signals.signalData_dispo.connect(self.remplir_tableau_cmr)
#        self.threadpool.start(bdd_thread)
###        bdd_thread.run()
#        
#        self.thread_combobox = Gestion_Combobox_domaine_Thread(self.engine)
#        self.thread_combobox.signals.signalmodel_dispo.connect(self.affectation_model_combobox_domaine)
##        self.thread_combobox.finished.connect(self.danslemille)
#        self.threadpool.start(self.thread_combobox)
#        
#        print(self.thread_combobox)
##        self.thread_combobox.run()
#        
#    @pyqtSlot(QStandardItemModel)
#    def affectation_model_combobox_domaine(self, model):
#        """permet de recevoir le model créé et affecte au combobox dans le thread specifique"""
#        print("jy suis")
#        mutex = QMutex()
#        mutex.lock()
#        self.model = model
#        self.comboBox_domaine.setModel(self.model)
#
#        self.thread_finish = True
#        mutex.unlock()
#        print(self.thread_finish)
        
    
    @pyqtSlot(list)
    def remplir_tableau_cmr(self, gen_list_cmr):
        
        self.tableWidget.setRowCount(0)
        for cmr in reversed(gen_list_cmr):
#            print(cmr)
            self.tableWidget.insertRow(0)
            
            
            item_nom = QTableWidgetItem(cmr.NOM)
            item_prenom = QTableWidgetItem(cmr.PRENOM)
            
            self.tableWidget.setItem(0, 0, item_nom)
            self.tableWidget.setItem(0, 1, item_prenom)
            
            self.tableWidget.setCellWidget(0, 2, QComboBox())
            self.tableWidget.cellWidget (0, 2).addItems(["*", "Acquises", "À améliorer", "Non acquises"])
            
            self.tableWidget.setCellWidget(0, 3, QComboBox())          
            self.tableWidget.cellWidget (0, 3).addItems([str(x) for x in range(21)])
            
            self.tableWidget.setCellWidget(0, 4, QTextEdit())
            self.tableWidget.setCellWidget(0, 5, QCheckBox())
            
            
    @pyqtSlot()
    def on_pushButton_enregistrer_clicked(self):
        """
        Slot documentation goes here.
        """

        nom_formation = self.lineEdit_nom_formation.text()
        if nom_formation:
            date = self.dateEdit.date().toString("dd-MM-yyyy")
            type_formation = self.comboBox_type_formation.currentText()
#            domaine = self.comboBox_domaine.currentText()
            domaine=[]
            for ligne in range(self.model.rowCount()):
                if self.model.item(ligne, 0).checkState() == Qt.Checked:
                    domaine.append(self.model.item(ligne, 0).text())
            
            plan = self.textEdit_plan_formation.toPlainText()
            
            nbr_ligne = self.tableWidget.rowCount()
            sauvegarde_dico = []
            for ligne in range(nbr_ligne):
                if self.tableWidget.cellWidget (ligne, 5).isChecked():
                    nom = self.tableWidget.item(ligne, 0).text()
                    prenom = self.tableWidget.item(ligne, 1).text()
                    gen_id = self.cmr_bdd.recup_id_cmr(nom, prenom)
                    try:
                        resultat = self.tableWidget.cellWidget (ligne, 2).currentText()
                    except:
                        resultat = None
                    try:
                        note = self.tableWidget.cellWidget (ligne, 3).currentText()
                    except:
                        note = None
                    try:
                        remarque = self.tableWidget.item(ligne, 4).text()
                    except:
                        remarque = None
                   
                    dico = {"nom": nom, 
                            "prenom": prenom,
                            "id": gen_id,  
                            "resultat": resultat, 
                            "note": note, 
                            "remarque": remarque}
#                    print(dico)
                    sauvegarde_dico.append(json.dumps(dico))
            
            sauvegarde = {"nom_formation":nom_formation,"date": date, 
                            "type_formation": type_formation, "domaine":domaine,  
                            "plan": plan, "participants":sauvegarde_dico}

#            print(sauvegarde)
            
            if self.windowTitle() == "Enregistrement d'une formation":
                self.cmr_bdd.insertion_formation(sauvegarde)                
                self.close()                
                self.fermeture_reouverture.emit()
            else: #on est dans une modification
                self.cmr_bdd.modif_formation(self.id_formation_a_modif, sauvegarde)                
                self.close()
                self.maj.emit()
    
    @pyqtSlot(object)
    def reaffectation_formation(self, formation):
        """fct qui reaffecte les donnees recues par le signal"""
        
        self.setWindowTitle ("Modification d'une formation")
#        print(formation)
        
        self.id_formation_a_modif = formation.ID
#        print(formation.ID)
        
        self.lineEdit_nom_formation.setText(formation.NOM_FORMATION)
        self.dateEdit.setDate(formation.DATE_FORMATION)
        
        index = self.comboBox_type_formation.findText(formation.TYPE_FORMATION, Qt.MatchExactly)
        if index:
            self.comboBox_type_formation.setCurrentIndex(index)

        #gestion des domaines :
        for domaine in formation.DOMAINE:
            for ligne in range(self.model.rowCount()):
#                print(f"ligne {ligne}")
                if self.model.item(ligne, 0).text() == domaine:
                    self.model.item(ligne, 0).setData(Qt.Checked, Qt.CheckStateRole)

        self.textEdit_plan_formation.setText(formation.PLAN)
        
        
        for participant in formation.LIST_PARTICIPANTS:
            nom = json.loads(participant)["nom"]
            prenom = json.loads(participant)["prenom"]
#            id = json.loads(participant)["id"]
            resultat = json.loads(participant)["resultat"]
            note = json.loads(participant)["note"]
            remarque = json.loads(participant)["remarque"]
        
            for ligne in range(self.tableWidget.rowCount()):
                
                if self.tableWidget.item(ligne, 0).text() == nom and self.tableWidget.item(ligne, 1).text() == prenom :
                    
                    index = self.tableWidget.cellWidget(ligne, 2).findText(resultat, Qt.MatchExactly)
                    if index != -1 :
                        self.tableWidget.cellWidget(ligne, 2).setCurrentIndex(index)
                    
                    index = self.tableWidget.cellWidget(ligne, 3).findText(note, Qt.MatchExactly)
                    if index != -1 :
                        self.tableWidget.cellWidget(ligne, 3).setCurrentIndex(index)
        
                    self.tableWidget.cellWidget(ligne, 4).setText(remarque)
                    
                    self.tableWidget.cellWidget(ligne, 5).setChecked(True)
        

class Gestion_Combobox_domaine_Thread (QRunnable):
    
#    signalmodel_dispo = pyqtSignal(QStandardItemModel)
    
    def __init__(self, engine):
        QThread.__init__(self)
        
        self.signals = WorkerSignals()
#        self.combobox = combobox
        self.engine = engine
        
#    def __del__(self):
#        self.wait()
        
    def run(self):
        """rempli le combobox domaine et cree la possibilité de checked des items"""
        
        init_domaine = Insertion_Domaine(self.engine)
        areas = init_domaine.recuperation_domaine()
        
        self.model = QStandardItemModel((len(areas)+1), 1)# 5 rows, 1 col
        
        firstItem = QStandardItem("---- Select domaine(s) ----")
        firstItem.setBackground(QBrush(QColor(200, 200, 200)))
        firstItem.setSelectable(False)
        self.model.setItem(0, 0, firstItem)
        
        for i,area in enumerate(areas):
            item = QStandardItem(area)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
            self.model.setItem(i+1, 0, item)
        
        
        self.signals.signalmodel_dispo.emit(self.model)

#        self.finished.emit()
        
        
class Gestion_BDD_Thread(QRunnable):
    
    signalData_dispo = pyqtSignal(list)
    
    def __init__(self, cmr_bdd):
        QThread.__init__(self)
        
        self.cmr_bdd = cmr_bdd
        self.signals = WorkerSignals()
        
#    def __del__(self):
#        self.wait()
        
    def run(self):
               
        self.signals.signalData_dispo.emit(next(self.cmr_bdd.recup_cmr_en_activite()))
        
        
        
class WorkerSignals(QObject):
    '''
        Gestion des signaux

    '''
    signalmodel_dispo = pyqtSignal(QStandardItemModel)
    
    signalData_dispo = pyqtSignal(list)
    
    
    
    
    
    
    
    
