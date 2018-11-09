# -*- coding: utf-8 -*-

"""
Module implementing Main_Formation.
"""

from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QMainWindow, QTextEdit, QTableWidgetItem, QTableWidget, QListWidget , QMessageBox

from .Ui_Main_Formation import Ui_Main_Formation
from GUI.Formation import Formation
from Package.AccesBdd import Bdd_Cmr
from Package.Documents_de_Formation import Attestation_formation
import json
import pendulum
class Main_Formation(QMainWindow, Ui_Main_Formation):
    """
    Class documentation goes here.
    
    """
    
    #signal
    formation_a_modifier = pyqtSignal(object)
    
    def __init__(self, engine, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        
        self.engine = engine
        self.db_formation = Bdd_Cmr(self.engine)
        self.remplir_tableau_recap()
    
    def remplir_tableau_recap(self):
#        formations = 
#        print("test")
        self.tableWidget_recap.setRowCount(0)
        
        for formation in next(self.db_formation.recup_formation()):
            self.tableWidget_recap.insertRow(0)
            self.tableWidget_recap.setRowHeight(0, 300)
            
#            print(formation.LIST_PARTICIPANTS)
            nom_formation = QTableWidgetItem(formation.NOM_FORMATION)
#            print(formation.NOM_FORMATION)
            date_formation = QTableWidgetItem(str(formation.DATE_FORMATION))
            type_formation= QTableWidgetItem(formation.TYPE_FORMATION)
            
            domaine = formation.DOMAINE

            self.tableWidget_recap.setItem(0, 0, nom_formation)
            self.tableWidget_recap.setItem(0, 1, date_formation)
            self.tableWidget_recap.setItem(0, 2, type_formation)
            
            self.tableWidget_recap.setCellWidget(0, 3, QListWidget())
            try:
                self.tableWidget_recap.cellWidget(0, 3).addItems (domaine)            
            except:
                pass
                
            self.tableWidget_recap.setCellWidget(0, 4, QTextEdit())
            try:
                self.tableWidget_recap.cellWidget(0, 4).setPlainText(formation.PLAN)
            except:
                pass
            
            self.tableWidget_recap.setCellWidget(0, 5, QTableWidget())
            list_key =list(json.loads(formation.LIST_PARTICIPANTS[0]).keys())
            for ele in reversed(list_key):
                self.tableWidget_recap.cellWidget(0, 5).insertColumn(0)
                
#            print(list(json.loads(formation.LIST_PARTICIPANTS[0]).keys()))
            self.tableWidget_recap.cellWidget(0, 5).setHorizontalHeaderLabels(list_key)
#            try:
                
            for participant in formation.LIST_PARTICIPANTS:
#                print(participant)
                self.tableWidget_recap.cellWidget(0, 5).insertRow(0)
                
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 0, QTableWidgetItem(json.loads(participant)["nom"]))
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 1, QTableWidgetItem(json.loads(participant)["prenom"]))
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 2, QTableWidgetItem(str(json.loads(participant)["id"])))
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 3, QTableWidgetItem(json.loads(participant)["resultat"]))
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 4, QTableWidgetItem(json.loads(participant)["note"]))
                self.tableWidget_recap.cellWidget(0, 5).setItem(0, 5, QTableWidgetItem(json.loads(participant)["remarque"]))
                
#                print(json.loads(participant))
                
#                self.tableWidget_recap.cellWidget(0, 5).append(json.loads(participant).items())
#            except:
#                pass
#            
#               self.tableWidget_recap.resizeRowsToContents()
        self.tableWidget_recap.resizeColumnsToContents()
        self.tableWidget_recap.verticalHeader().setStretchLastSection(True)
            
        self.tableWidget_recap.setColumnWidth(5, 625);
    @pyqtSlot()
    def on_actionNouvelle_Formation_triggered(self):
        """
        Slot documentation goes here.
        """
        
        def gestion_signal_fermeture_ouverture():
            """fct qui permet de nettoyer et mettre a jour le tableau recap et de reouvrir une
            gui formation pour une autre saisie"""
            
            self.remplir_tableau_recap()            
            self.on_actionNouvelle_Formation_triggered()
            
#        global saisie_formation
        self.saisie_formation = Formation(self.engine, self)
        self.saisie_formation.fermeture_reouverture.connect(gestion_signal_fermeture_ouverture)
        
        self.saisie_formation.show()
    
    @pyqtSlot()
    def on_actionModifier_Formation_triggered(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget_recap.currentRow()
        column = self.tableWidget_recap.currentColumn()
        
#        if row:
        self.on_tableWidget_recap_cellDoubleClicked(row, column)
#        else:
#            QMessageBox.warning(
#                self,
#                self.trUtf8("Attestation de Presence"),
#                self.trUtf8("""Merci de selectionner la ligne correspondante à la formation"""))
    
    @pyqtSlot(int, int)
    def on_tableWidget_recap_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        """
#        print(f"ligne {row} et colonne {column}")
        name_formation = self.tableWidget_recap.item(row, 0).text()
        date = self.tableWidget_recap.item(row, 1).text()
#        print(date)
#        print(self.tableWidget_recap.cellWidget(0, 3).count())
        domaine = []
        for i in range(self.tableWidget_recap.cellWidget(0, 3).count()):
            try:
                domaine.append(self.tableWidget_recap.cellWidget(row, 3).item(i).text())
            except:
#                print(self.tableWidget_recap.cellWidget(row, 3).item(i))
                pass
#        domaine = [self.tableWidget_recap.cellWidget(row, 3).item(i).text() for i in range(self.tableWidget_recap.cellWidget(0, 3).count())]
        
#        print(domaine)
        
        type_formation = self.tableWidget_recap.item(row, 2).text()
        formation = self.db_formation.recup_formation_particuliere(name_formation, date, domaine, type_formation)
        
        self.saisie_formation = Formation(self.engine, self)
        self.saisie_formation.maj.connect(self.remplir_tableau_recap)
        self.saisie_formation.show()
        
        self.formation_a_modifier.emit(formation)
    
    @pyqtSlot()
    def on_actionAttestation_de_presence_triggered(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget_recap.currentRow()
        print(row)
#        if row:
        try:
            nom_formation  = self.tableWidget_recap.item(row, 0).text()
        except:
            nom_formation = None
            
#        try:

        date  = pendulum.parse(self.tableWidget_recap.item(row, 1).text(), exact= True).format('%A %d %B %Y', locale='fr')


        try:
            domaine  = self.tableWidget_recap.cellWidget(row, 3).toPlainText()
        except:
            domaine = None
            
        try:
            type_formation  = self.tableWidget_recap.item(row, 2).text()
        except:
            type_formation = None

        plan  = self.tableWidget_recap.cellWidget(row, 4).toPlainText()#[self.tableWidget_recap.cellWidget(row, 4).item(i).text() for i in range(self.tableWidget_recap.cellWidget(0, 4).count())]#self.tableWidget_recap.cellWidget(row, 3).toPlainText()

        
        lignetableau= []
        for ligne in range(self.tableWidget_recap.cellWidget(row,5 ).rowCount()):
            tableau_dic ={"nom":self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 0).text(), 
                           "prenom": self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 1).text(), 
                            "id":self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 2).text(), 
                            "resultat":self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 3).text(),
                            "note":self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 4).text(),
                            "remarque" : self.tableWidget_recap.cellWidget(row,5 ).item(ligne, 5).text()}
            lignetableau.append(tableau_dic)
            
            
        donnees = {"nom_formation": nom_formation, 
                    "date" : date,  
                    "domaine": domaine, 
                    "type_formation": type_formation, 
                    "plan": plan , 
                    "tableau_resultats" : lignetableau}
                    
                    
#            print(donnees)

#        
#        
        formation = Attestation_formation(donnees)
        formation.document_presence()
        
#        else:
#            QMessageBox.warning(
#                self,
#                self.trUtf8("Attestation de Presence"),
#                self.trUtf8("""Merci de selectionner la ligne correspondante à la formation"""))
#            
    
    @pyqtSlot()
    def on_actionHabilitations_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
