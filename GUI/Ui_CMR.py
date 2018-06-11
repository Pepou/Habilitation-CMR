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

class Ui_Habilitation_CMR(object):
    def setupUi(self, Habilitation_CMR):
        Habilitation_CMR.setObjectName(_fromUtf8("Habilitation_CMR"))
        Habilitation_CMR.resize(814, 600)
        self.centralWidget = QtGui.QWidget(Habilitation_CMR)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setWrapping(False)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dateEdit)
        self.lineEdit_cmr = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_cmr.setObjectName(_fromUtf8("lineEdit_cmr"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_cmr)
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.verticalLayout.addWidget(self.tableWidget)
        Habilitation_CMR.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Habilitation_CMR)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuExporter = QtGui.QMenu(self.menuBar)
        self.menuExporter.setObjectName(_fromUtf8("menuExporter"))
        Habilitation_CMR.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuExporter.menuAction())

        self.retranslateUi(Habilitation_CMR)
        QtCore.QMetaObject.connectSlotsByName(Habilitation_CMR)

    def retranslateUi(self, Habilitation_CMR):
        Habilitation_CMR.setWindowTitle(_translate("Habilitation_CMR", "MainWindow", None))
        self.label.setText(_translate("Habilitation_CMR", "Date  ", None))
        self.label_2.setText(_translate("Habilitation_CMR", "Recherche Correspondant", None))
        self.label_3.setText(_translate("Habilitation_CMR", "Type d\'habilitation", None))
        self.comboBox.setItemText(0, _translate("Habilitation_CMR", "Contrôle de maintien / extension de l\'habilitation", None))
        self.comboBox.setItemText(1, _translate("Habilitation_CMR", "Habilitation avant prise de poste", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Habilitation_CMR", "NOM", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Habilitation_CMR", "PRENOM", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Habilitation_CMR", "DATE_FORMATION_INITIALE", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Habilitation_CMR", "EXCEL", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Habilitation_CMR", "F_CARTOGRAPHIE", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Habilitation_CMR", "F_TEMPERATURE", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Habilitation_CMR", "F_VITESSE/TEMPS/MASSE", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Habilitation_CMR", "PIPETTE", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Habilitation_CMR", "ACTE_TEMPS", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Habilitation_CMR", "ACTE_VITESSE", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Habilitation_CMR", "ACTE_TEMPRATURE", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Habilitation_CMR", "ACTE_CARTO", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Habilitation_CMR", "INTRA_CARTO", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Habilitation_CMR", "INTRA_VITESSE_TEMPS", None))
        self.menuExporter.setTitle(_translate("Habilitation_CMR", "Exporter", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Habilitation_CMR = QtGui.QMainWindow()
    ui = Ui_Habilitation_CMR()
    ui.setupUi(Habilitation_CMR)
    Habilitation_CMR.show()
    sys.exit(app.exec_())

