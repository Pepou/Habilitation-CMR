# -*- coding: utf-8 -*-

"""
Module implementing Gestion_CMR.
"""

from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QMainWindow, QTableWidgetItem

from .Ui_CMR import Ui_Gestion_CMR
from Package.AccesBdd import Bdd_Cmr, Insertion_Domaine

from GUI.Main_Formation import Main_Formation



class Gestion_CMR(QMainWindow, Ui_Gestion_CMR):
    """
    Class documentation goes here.
    """
    def __init__(self, engine, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        
        self.engine = engine
        self.cmr_bdd = Bdd_Cmr(self.engine)
#        self.cmr_bdd.recup_cmr()
        self.remplir_tableau_cmr(self.cmr_bdd.recup_cmr())
        


#            print(cmr.NOM)
    def remplir_tableau_cmr(self, gen_list_cmr):
        self.tableWidget_cmr.setRowCount(0)
        for cmr in reversed(next(gen_list_cmr)):
            self.tableWidget_cmr.insertRow(0)
            item_nom = QTableWidgetItem(cmr.NOM)
            item_prenom = QTableWidgetItem(cmr.PRENOM)
            item_courriel = QTableWidgetItem(cmr.COURRIEL)
            item_fonction = QTableWidgetItem(cmr.FONCTION)
            item_site = QTableWidgetItem(cmr.SITE)
            item_service = QTableWidgetItem(cmr.SERVICE)
            item_responsable = QTableWidgetItem(cmr.RESPONSABLE)
            
            if not cmr.ARCHIVAGE:
                item_en_activite = QTableWidgetItem("Oui")
            else:
                item_en_activite = QTableWidgetItem("Non")
            self.tableWidget_cmr.setItem(0, 0, item_nom)
            self.tableWidget_cmr.setItem(0, 1, item_prenom)
            self.tableWidget_cmr.setItem(0, 2, item_courriel)
            self.tableWidget_cmr.setItem(0, 3, item_fonction)
            self.tableWidget_cmr.setItem(0, 4, item_site)
            self.tableWidget_cmr.setItem(0, 5, item_service)
            self.tableWidget_cmr.setItem(0, 6, item_responsable)
            self.tableWidget_cmr.setItem(0, 7, item_en_activite)
            
            self.tableWidget_cmr.resizeColumnsToContents()
    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        """
        Slot documentation goes here.
        """
        if self.tabWidget.currentIndex() == 1:
            #creation CMR:
            self.comboBox_site.clear()
            sites = self.cmr_bdd.recup_site()
            self.comboBox_site.addItems([x[0] for x in next(sites)])
            
    
    @pyqtSlot(str)
    def on_lineEdit_recherche_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
                
        tri_cmr = self.cmr_bdd.recherche(p0)
        self.remplir_tableau_cmr(tri_cmr)
    
    @pyqtSlot(str)
    def on_comboBox_site_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        self.comboBox_service.clear()
#        site = 
        services = self.cmr_bdd.recupe_services_par_site(p0)
        self.comboBox_service.addItems([x[0] for x in next(services)])
    
    @pyqtSlot()
    def on_pushButton_enregistrer_nouv_cmr_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            for ele in [self.comboBox_site.currentText(), self.comboBox_service.currentText()
                        ,self.lineEdit_nom.text(), self.lineEdit_prenom.text() ]:
                if not ele:
                    raise ValueError
            
            new_cmr = {"site":self.comboBox_site.currentText(), 
                        "service": self.comboBox_service.currentText(), 
                        "responsable":self.lineEdit_responsable.text().upper(), 
                        "nom":self.lineEdit_nom.text().upper(), 
                        "prenom":self.lineEdit_prenom.text().upper(), 
                        "courriel":self.lineEdit_courriel.text(), 
                        "fonction":self.lineEdit_fonction.text()}
            
            self.cmr_bdd.insertion_new_cmr(new_cmr)
        
            self.nettoyage_onglet_creation_cmr()
            self.tabWidget.setCurrentIndex(0)
            self.remplir_tableau_cmr(self.cmr_bdd.recup_cmr())
        
        except ValueError:
            print("merci de saisir toutes les informations")
            pass
            
    def nettoyage_onglet_creation_cmr(self):
        """permet de remettre à zero longlet de creation et de revenir sur l'onglet de base"""
        
        self.comboBox_site.setCurrentIndex(0)
        self.lineEdit_responsable.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_prenom.clear()
        self.lineEdit_courriel.clear()
        self.lineEdit_fonction.clear()
    
    @pyqtSlot(int, int)
    def on_tableWidget_cmr_cellDoubleClicked(self, row, column):
        """
        telehcarge les donnees du tableau pour les mettre dans l'onglet modif
        """
        self.tabWidget.setCurrentIndex(2)
        
        self.lineEdit_nom_modif.setText(self.tableWidget_cmr.item(row,0).text())
        self.lineEdit_prenom_modif.setText(self.tableWidget_cmr.item(row,1).text())
        self.lineEdit_responsable_2.setText(self.tableWidget_cmr.item(row,6).text())
        self.lineEdit_courriel_2.setText(self.tableWidget_cmr.item(row,2).text())
        self.lineEdit_fonction_2.setText(self.tableWidget_cmr.item(row,3).text())
        
        
        self.comboBox_site_modif.clear()
        sites = self.cmr_bdd.recup_site()
        self.comboBox_site_modif.addItems([x[0] for x in next(sites)])
        
        index_site = self.comboBox_site_modif.findText(self.tableWidget_cmr.item(row,4).text(),Qt.MatchContains)
        if index_site != -1:
            self.comboBox_site_modif.setCurrentIndex(index_site)
            
        self.comboBox_service_modif.clear()
        services = self.cmr_bdd.recupe_services_par_site(self.comboBox_site_modif.currentText())
        self.comboBox_service_modif.addItems([x[0] for x in next(services)])
        
        index_service = self.comboBox_service_modif.findText(self.tableWidget_cmr.item(row,5).text(),Qt.MatchContains)
        if index_site != -1:
            self.comboBox_service_modif.setCurrentIndex(index_service)
        
        if self.tableWidget_cmr.item(row,7).text() == "Oui":
            self.comboBox_en_activit.setCurrentIndex(0)
        else:
            self.comboBox_en_activit.setCurrentIndex(1)
        
        #self.id est un generator
        self.id = self.cmr_bdd.recup_id_cmr(self.tableWidget_cmr.item(row,0).text(), 
                                        self.tableWidget_cmr.item(row,1).text())   

    
    @pyqtSlot(str)
    def on_comboBox_site_modif_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        self.comboBox_service_modif.clear()
#        site = 
        services = self.cmr_bdd.recupe_services_par_site(p0)
        self.comboBox_service_modif.addItems([x[0] for x in next(services)])
    
    @pyqtSlot()
    def on_pushButton_modifier_clicked(self):
        """
        Slot documentation goes here.
        """
#        print("couuc")
        
        if self.comboBox_en_activit.currentText()== "Oui":
            activite = False #dans la base on parle d'archivage
        else:
            activite = True
        cmr_modif= {"id":self.id, "nom": self.lineEdit_nom_modif.text(), 
                    "prenom":self.lineEdit_prenom_modif.text(), "responsable": self.lineEdit_responsable_2.text(), 
                    "courriel": self.lineEdit_courriel_2.text(), "fonction":self.lineEdit_fonction_2.text(), 
                    "site":self.comboBox_site_modif.currentText(), "service":self.comboBox_service_modif.currentText(), 
                    "activite":activite}
        self.cmr_bdd.modif_cmr(cmr_modif)
#        print(f"dans le bouton {cmr_modif}")
        self.nettoyage_onglet_modif()
        
        self.tabWidget.setCurrentIndex(0)
        self.remplir_tableau_cmr(self.cmr_bdd.recup_cmr())
    
    @pyqtSlot()
    def on_pushButton_annul_modif_clicked(self):
        """
        Slot documentation goes here.
        """
        self.nettoyage_onglet_modif()
        self.tabWidget.setCurrentIndex(0)
    
    def nettoyage_onglet_modif(self):
        """permet de netooyer l'ongelt modif et revenir à l'ingelt de base"""
        
        self.lineEdit_nom_modif.clear()
        self.lineEdit_prenom_modif.clear()
        self.lineEdit_responsable_2.clear()
        self.lineEdit_courriel_2.clear()
        self.lineEdit_fonction_2.clear()
        self.comboBox_site_modif.clear()
        self.comboBox_service_modif.clear()
        self.comboBox_en_activit.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_pushButton_annule_creation_clicked(self):
        """
        Slot documentation goes here.
        """
        self.nettoyage_onglet_creation_cmr()
        self.tabWidget.setCurrentIndex(0)
    
#    @pyqtSlot()
#    def on_actionNouvelle_Formation_triggered(self):
#        """
#        Slot documentation goes here.
#        """
##        app = QApplication(sys.argv)
##        self.close()
##        global formation
#        self.formation = Main_Formation(self.engine)
#        self.formation.show()
#        
#        
##        saisie_formation.show()
    

    @pyqtSlot()
    def on_actionModule_Formation_triggered(self):
        """
        Slot documentation goes here.
        """
#        print("coucou")
        self.formation = Main_Formation(self.engine)
        self.formation.show()
#        self.hide()
