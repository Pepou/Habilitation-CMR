# -*- coding: utf-8 -*-

"""
Module implementing Gestion_CMR.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow, QTableWidgetItem

from .Ui_CMR import Ui_Gestion_CMR
from Package.AccesBdd import Bdd_Cmr

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
        
        self.cmr_bdd = Bdd_Cmr(engine)
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
                        "responsable":self.lineEdit_responsable.text(), 
                        "nom":self.lineEdit_nom.text(), 
                        "prenom":self.lineEdit_prenom.text(), 
                        "courriel":self.lineEdit_courriel.text(), 
                        "fonction":self.lineEdit_fonction.text()}
        
            self.cmr_bdd.insertion_new_cmr(new_cmr)
        except ValueError:
            print("merci de saisir toutes les informations")
            pass
