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
        Gestion_CMR.resize(814, 557)
        self.centralWidget = QtGui.QWidget(Gestion_CMR)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox_site = QtGui.QComboBox(self.tab_2)
        self.comboBox_site.setObjectName(_fromUtf8("comboBox_site"))
        self.verticalLayout_3.addWidget(self.comboBox_site)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox_service = QtGui.QComboBox(self.tab_2)
        self.comboBox_service.setObjectName(_fromUtf8("comboBox_service"))
        self.verticalLayout_3.addWidget(self.comboBox_service)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.lineEdit_responsable = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_responsable.setObjectName(_fromUtf8("lineEdit_responsable"))
        self.verticalLayout_3.addWidget(self.lineEdit_responsable)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit_nom = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.verticalLayout_3.addWidget(self.lineEdit_nom)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_prenom = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_prenom.setObjectName(_fromUtf8("lineEdit_prenom"))
        self.verticalLayout_3.addWidget(self.lineEdit_prenom)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.lineEdit_courriel = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_courriel.setObjectName(_fromUtf8("lineEdit_courriel"))
        self.verticalLayout_3.addWidget(self.lineEdit_courriel)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit_fonction = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_fonction.setObjectName(_fromUtf8("lineEdit_fonction"))
        self.verticalLayout_3.addWidget(self.lineEdit_fonction)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_enregistrer_nouv_cmr = QtGui.QPushButton(self.tab_2)
        self.pushButton_enregistrer_nouv_cmr.setObjectName(_fromUtf8("pushButton_enregistrer_nouv_cmr"))
        self.horizontalLayout_3.addWidget(self.pushButton_enregistrer_nouv_cmr)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_5.addWidget(self.label_15)
        self.lineEdit_nom_modif = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_nom_modif.setObjectName(_fromUtf8("lineEdit_nom_modif"))
        self.horizontalLayout_5.addWidget(self.lineEdit_nom_modif)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.lineEdit_prenom_modif = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_prenom_modif.setObjectName(_fromUtf8("lineEdit_prenom_modif"))
        self.horizontalLayout_6.addWidget(self.lineEdit_prenom_modif)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_4.addWidget(self.label_13)
        self.comboBox_site_modif = QtGui.QComboBox(self.tab_3)
        self.comboBox_site_modif.setObjectName(_fromUtf8("comboBox_site_modif"))
        self.verticalLayout_4.addWidget(self.comboBox_site_modif)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_5.addWidget(self.label_9)
        self.comboBox_service_modif = QtGui.QComboBox(self.tab_3)
        self.comboBox_service_modif.setObjectName(_fromUtf8("comboBox_service_modif"))
        self.verticalLayout_5.addWidget(self.comboBox_service_modif)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_6.addWidget(self.label_12)
        self.lineEdit_responsable_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_responsable_2.setObjectName(_fromUtf8("lineEdit_responsable_2"))
        self.verticalLayout_6.addWidget(self.lineEdit_responsable_2)
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_6.addWidget(self.label_10)
        self.lineEdit_courriel_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_courriel_2.setObjectName(_fromUtf8("lineEdit_courriel_2"))
        self.verticalLayout_6.addWidget(self.lineEdit_courriel_2)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_6.addWidget(self.label_11)
        self.lineEdit_fonction_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_fonction_2.setObjectName(_fromUtf8("lineEdit_fonction_2"))
        self.verticalLayout_6.addWidget(self.lineEdit_fonction_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox_en_activit = QtGui.QComboBox(self.tab_3)
        self.comboBox_en_activit.setObjectName(_fromUtf8("comboBox_en_activit"))
        self.comboBox_en_activit.addItem(_fromUtf8(""))
        self.comboBox_en_activit.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox_en_activit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_modifier = QtGui.QPushButton(self.tab_3)
        self.pushButton_modifier.setObjectName(_fromUtf8("pushButton_modifier"))
        self.horizontalLayout_4.addWidget(self.pushButton_modifier)
        self.pushButton_annul_modif = QtGui.QPushButton(self.tab_3)
        self.pushButton_annul_modif.setObjectName(_fromUtf8("pushButton_annul_modif"))
        self.horizontalLayout_4.addWidget(self.pushButton_annul_modif)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(769, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        Gestion_CMR.setCentralWidget(self.centralWidget)

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
        self.pushButton_2.setText(_translate("Gestion_CMR", "Annuler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Gestion_CMR", "Creation Correspondant", None))
        self.label_15.setText(_translate("Gestion_CMR", "NOM", None))
        self.label_16.setText(_translate("Gestion_CMR", "PRENOM", None))
        self.label_13.setText(_translate("Gestion_CMR", "SITE", None))
        self.label_9.setText(_translate("Gestion_CMR", "SERVICE", None))
        self.label_12.setText(_translate("Gestion_CMR", "RESPONSABLE", None))
        self.label_10.setText(_translate("Gestion_CMR", "COURRIEL", None))
        self.label_11.setText(_translate("Gestion_CMR", "FONCTION", None))
        self.label_8.setText(_translate("Gestion_CMR", "En activité", None))
        self.comboBox_en_activit.setItemText(0, _translate("Gestion_CMR", "Oui", None))
        self.comboBox_en_activit.setItemText(1, _translate("Gestion_CMR", "Non", None))
        self.pushButton_modifier.setText(_translate("Gestion_CMR", "Modifier", None))
        self.pushButton_annul_modif.setText(_translate("Gestion_CMR", "Annuler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Gestion_CMR", "Modification Correspondant", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Gestion_CMR = QtGui.QMainWindow()
    ui = Ui_Gestion_CMR()
    ui.setupUi(Gestion_CMR)
    Gestion_CMR.show()
    sys.exit(app.exec_())

