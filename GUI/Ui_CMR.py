# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Developpement Informatique\Python\Habilitation CMR\GUI\CMR.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Gestion_CMR(object):
    def setupUi(self, Gestion_CMR):
        Gestion_CMR.setObjectName(_fromUtf8("Gestion_CMR"))
        Gestion_CMR.resize(856, 688)
        self.centralWidget = QtGui.QWidget(Gestion_CMR)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_recherche = QtGui.QLabel(self.tab)
        self.label_recherche.setObjectName(_fromUtf8("label_recherche"))
        self.horizontalLayout.addWidget(self.label_recherche)
        self.lineEdit_recherche = QtGui.QLineEdit(self.tab)
        self.lineEdit_recherche.setObjectName(_fromUtf8("lineEdit_recherche"))
        self.horizontalLayout.addWidget(self.lineEdit_recherche)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget_cmr = QtGui.QTableWidget(self.tab)
        self.tableWidget_cmr.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_cmr.setAlternatingRowColors(True)
        self.tableWidget_cmr.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_cmr.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_cmr.setObjectName(_fromUtf8("tableWidget_cmr"))
        self.tableWidget_cmr.setColumnCount(8)
        self.tableWidget_cmr.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_cmr.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.tableWidget_cmr)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(40)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_site = QtGui.QComboBox(self.tab_2)
        self.comboBox_site.setObjectName(_fromUtf8("comboBox_site"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_site)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_service = QtGui.QComboBox(self.tab_2)
        self.comboBox_service.setObjectName(_fromUtf8("comboBox_service"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_service)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_responsable = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_responsable.setObjectName(_fromUtf8("lineEdit_responsable"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_responsable)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_nom = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_nom)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_prenom = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_prenom.setObjectName(_fromUtf8("lineEdit_prenom"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_prenom)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_courriel = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_courriel.setObjectName(_fromUtf8("lineEdit_courriel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_courriel)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_fonction = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_fonction.setObjectName(_fromUtf8("lineEdit_fonction"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_fonction)
        spacerItem = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_2.setItem(7, QtGui.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_enregistrer_nouv_cmr = QtGui.QPushButton(self.tab_2)
        self.pushButton_enregistrer_nouv_cmr.setObjectName(_fromUtf8("pushButton_enregistrer_nouv_cmr"))
        self.horizontalLayout_3.addWidget(self.pushButton_enregistrer_nouv_cmr)
        self.pushButton_annule_creation = QtGui.QPushButton(self.tab_2)
        self.pushButton_annule_creation.setObjectName(_fromUtf8("pushButton_annule_creation"))
        self.horizontalLayout_3.addWidget(self.pushButton_annule_creation)
        self.formLayout_2.setLayout(8, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_nom_modif = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_nom_modif.setObjectName(_fromUtf8("lineEdit_nom_modif"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_nom_modif)
        self.lineEdit_prenom_modif = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_prenom_modif.setObjectName(_fromUtf8("lineEdit_prenom_modif"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_prenom_modif)
        self.label_13 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_13)
        self.comboBox_site_modif = QtGui.QComboBox(self.tab_3)
        self.comboBox_site_modif.setObjectName(_fromUtf8("comboBox_site_modif"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_site_modif)
        self.label_9 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.comboBox_service_modif = QtGui.QComboBox(self.tab_3)
        self.comboBox_service_modif.setObjectName(_fromUtf8("comboBox_service_modif"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_service_modif)
        self.label_12 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_responsable_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_responsable_2.setObjectName(_fromUtf8("lineEdit_responsable_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_responsable_2)
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_courriel_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_courriel_2.setObjectName(_fromUtf8("lineEdit_courriel_2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_courriel_2)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_fonction_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_fonction_2.setObjectName(_fromUtf8("lineEdit_fonction_2"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_fonction_2)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBox_en_activit = QtGui.QComboBox(self.tab_3)
        self.comboBox_en_activit.setObjectName(_fromUtf8("comboBox_en_activit"))
        self.comboBox_en_activit.addItem(_fromUtf8(""))
        self.comboBox_en_activit.addItem(_fromUtf8(""))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.comboBox_en_activit)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_modifier = QtGui.QPushButton(self.tab_3)
        self.pushButton_modifier.setObjectName(_fromUtf8("pushButton_modifier"))
        self.horizontalLayout_4.addWidget(self.pushButton_modifier)
        self.pushButton_annul_modif = QtGui.QPushButton(self.tab_3)
        self.pushButton_annul_modif.setObjectName(_fromUtf8("pushButton_annul_modif"))
        self.horizontalLayout_4.addWidget(self.pushButton_annul_modif)
        self.formLayout.setLayout(9, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        Gestion_CMR.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Gestion_CMR)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFormation = QtGui.QMenu(self.menuBar)
        self.menuFormation.setObjectName(_fromUtf8("menuFormation"))
        Gestion_CMR.setMenuBar(self.menuBar)
        self.actionNouvelle_Formation = QtGui.QAction(Gestion_CMR)
        self.actionNouvelle_Formation.setObjectName(_fromUtf8("actionNouvelle_Formation"))
        self.actionModule_Formation = QtGui.QAction(Gestion_CMR)
        self.actionModule_Formation.setObjectName(_fromUtf8("actionModule_Formation"))
        self.menuFormation.addAction(self.actionModule_Formation)
        self.menuBar.addAction(self.menuFormation.menuAction())

        self.retranslateUi(Gestion_CMR)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gestion_CMR)

    def retranslateUi(self, Gestion_CMR):
        Gestion_CMR.setWindowTitle(_translate("Gestion_CMR", "Gestion CMR", None))
        self.label_recherche.setText(_translate("Gestion_CMR", "Rechercher", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(0)
        item.setText(_translate("Gestion_CMR", "NOM", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(1)
        item.setText(_translate("Gestion_CMR", "PRENOM", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(2)
        item.setText(_translate("Gestion_CMR", "COURRIEL", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(3)
        item.setText(_translate("Gestion_CMR", "FONCTION", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(4)
        item.setText(_translate("Gestion_CMR", "SITE", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(5)
        item.setText(_translate("Gestion_CMR", "SERVICE", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(6)
        item.setText(_translate("Gestion_CMR", "RESPONSABLE", None))
        item = self.tableWidget_cmr.horizontalHeaderItem(7)
        item.setText(_translate("Gestion_CMR", "EN ACTIVITE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Gestion_CMR", "Visualisation des Correspondants", None))
        self.label_4.setText(_translate("Gestion_CMR", "SITE", None))
        self.label.setText(_translate("Gestion_CMR", "SERVICE", None))
        self.label_7.setText(_translate("Gestion_CMR", "RESPONSABLE", None))
        self.label_2.setText(_translate("Gestion_CMR", "NOM", None))
        self.label_3.setText(_translate("Gestion_CMR", "PRENOM", None))
        self.label_6.setText(_translate("Gestion_CMR", "COURRIEL", None))
        self.label_5.setText(_translate("Gestion_CMR", "FONCTION", None))
        self.pushButton_enregistrer_nouv_cmr.setText(_translate("Gestion_CMR", "Enregistrer", None))
        self.pushButton_annule_creation.setText(_translate("Gestion_CMR", "Annuler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Gestion_CMR", "Creation Correspondant", None))
        self.label_15.setText(_translate("Gestion_CMR", "NOM", None))
        self.label_16.setText(_translate("Gestion_CMR", "PRENOM", None))
        self.label_13.setText(_translate("Gestion_CMR", "SITE", None))
        self.label_9.setText(_translate("Gestion_CMR", "SERVICE", None))
        self.label_12.setText(_translate("Gestion_CMR", "RESPONSABLE", None))
        self.label_10.setText(_translate("Gestion_CMR", "COURRIEL", None))
        self.label_11.setText(_translate("Gestion_CMR", "FONCTION", None))
        self.label_8.setText(_translate("Gestion_CMR", "EN ACTIVITE", None))
        self.comboBox_en_activit.setItemText(0, _translate("Gestion_CMR", "Oui", None))
        self.comboBox_en_activit.setItemText(1, _translate("Gestion_CMR", "Non", None))
        self.pushButton_modifier.setText(_translate("Gestion_CMR", "Modifier", None))
        self.pushButton_annul_modif.setText(_translate("Gestion_CMR", "Annuler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Gestion_CMR", "Modification Correspondant", None))
        self.menuFormation.setTitle(_translate("Gestion_CMR", "Menu", None))
        self.actionNouvelle_Formation.setText(_translate("Gestion_CMR", "Module Formation", None))
        self.actionModule_Formation.setText(_translate("Gestion_CMR", "Module Formation", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Gestion_CMR = QtGui.QMainWindow()
    ui = Ui_Gestion_CMR()
    ui.setupUi(Gestion_CMR)
    Gestion_CMR.show()
    sys.exit(app.exec_())

