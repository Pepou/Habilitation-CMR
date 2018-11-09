# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Developpement Informatique\Python\Habilitation CMR\GUI\Formation.ui'
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

class Ui_Formation(object):
    def setupUi(self, Formation):
        Formation.setObjectName(_fromUtf8("Formation"))
        Formation.resize(800, 836)
        Formation.setStyleSheet(_fromUtf8("QLabel {\n"
"font:  10pt  \"Calibrii\" ;\n"
"font-weight: bold\n"
" }"))
        self.centralWidget = QtGui.QWidget(Formation)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_nom_formation = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_nom_formation.sizePolicy().hasHeightForWidth())
        self.lineEdit_nom_formation.setSizePolicy(sizePolicy)
        self.lineEdit_nom_formation.setObjectName(_fromUtf8("lineEdit_nom_formation"))
        self.verticalLayout_2.addWidget(self.lineEdit_nom_formation)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_type_formation = QtGui.QComboBox(self.centralWidget)
        self.comboBox_type_formation.setObjectName(_fromUtf8("comboBox_type_formation"))
        self.comboBox_type_formation.addItem(_fromUtf8(""))
        self.comboBox_type_formation.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.comboBox_type_formation)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboBox_domaine = QtGui.QComboBox(self.centralWidget)
        self.comboBox_domaine.setObjectName(_fromUtf8("comboBox_domaine"))
        self.verticalLayout_4.addWidget(self.comboBox_domaine)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.textEdit_plan_formation = QtGui.QTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_plan_formation.sizePolicy().hasHeightForWidth())
        self.textEdit_plan_formation.setSizePolicy(sizePolicy)
        self.textEdit_plan_formation.setObjectName(_fromUtf8("textEdit_plan_formation"))
        self.verticalLayout_5.addWidget(self.textEdit_plan_formation)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_7.addWidget(self.label_6)
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
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
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_enregistrer = QtGui.QPushButton(self.centralWidget)
        self.pushButton_enregistrer.setObjectName(_fromUtf8("pushButton_enregistrer"))
        self.horizontalLayout_3.addWidget(self.pushButton_enregistrer)
        self.pushButton_annuler = QtGui.QPushButton(self.centralWidget)
        self.pushButton_annuler.setObjectName(_fromUtf8("pushButton_annuler"))
        self.horizontalLayout_3.addWidget(self.pushButton_annuler)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        Formation.setCentralWidget(self.centralWidget)

        self.retranslateUi(Formation)
        QtCore.QMetaObject.connectSlotsByName(Formation)

    def retranslateUi(self, Formation):
        Formation.setWindowTitle(_translate("Formation", "MainWindow", None))
        self.label_4.setText(_translate("Formation", "Date de la formation", None))
        self.label.setText(_translate("Formation", "Nom de la formation", None))
        self.label_2.setText(_translate("Formation", "Type de formation", None))
        self.comboBox_type_formation.setItemText(0, _translate("Formation", "Continue", None))
        self.comboBox_type_formation.setItemText(1, _translate("Formation", "Initiale", None))
        self.label_3.setText(_translate("Formation", "Domaine", None))
        self.label_5.setText(_translate("Formation", "Plan de la formation", None))
        self.label_6.setText(_translate("Formation", "Tableau resultats", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Formation", "NOM", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Formation", "PRENOM", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Formation", "RESULTAT", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Formation", "NOTE", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Formation", "REMARQUE", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Formation", "PRESENCE", None))
        self.pushButton_enregistrer.setText(_translate("Formation", "Enregistrer", None))
        self.pushButton_annuler.setText(_translate("Formation", "Annuler", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Formation = QtGui.QMainWindow()
    ui = Ui_Formation()
    ui.setupUi(Formation)
    Formation.show()
    sys.exit(app.exec_())

