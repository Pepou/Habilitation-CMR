# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Developpement Informatique\Python\Habilitation CMR\GUI\Main_Formation.ui'
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

class Ui_Main_Formation(object):
    def setupUi(self, Main_Formation):
        Main_Formation.setObjectName(_fromUtf8("Main_Formation"))
        Main_Formation.resize(1488, 600)
        self.centralWidget = QtGui.QWidget(Main_Formation)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("QLabel{\n"
"background-color: rgb(170, 255, 255);\n"
"border: 1px solid Black;\n"
"border-radius: 5px;}"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.tableWidget_recap = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget_recap.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_recap.setFont(font)
        self.tableWidget_recap.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget_recap.setMouseTracking(True)
        self.tableWidget_recap.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget_recap.setWhatsThis(_fromUtf8(""))
        self.tableWidget_recap.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_recap.setAlternatingRowColors(True)
        self.tableWidget_recap.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_recap.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_recap.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_recap.setShowGrid(True)
        self.tableWidget_recap.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_recap.setWordWrap(True)
        self.tableWidget_recap.setCornerButtonEnabled(True)
        self.tableWidget_recap.setRowCount(0)
        self.tableWidget_recap.setObjectName(_fromUtf8("tableWidget_recap"))
        self.tableWidget_recap.setColumnCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_recap.setHorizontalHeaderItem(5, item)
        self.tableWidget_recap.horizontalHeader().setVisible(True)
        self.tableWidget_recap.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_recap.horizontalHeader().setHighlightSections(True)
        self.tableWidget_recap.verticalHeader().setVisible(True)
        self.tableWidget_recap.verticalHeader().setDefaultSectionSize(32)
        self.verticalLayout.addWidget(self.tableWidget_recap)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Main_Formation.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Main_Formation)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1488, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuNouvelle_Cartographie = QtGui.QMenu(self.menuBar)
        self.menuNouvelle_Cartographie.setObjectName(_fromUtf8("menuNouvelle_Cartographie"))
        self.menuDocuments = QtGui.QMenu(self.menuBar)
        self.menuDocuments.setObjectName(_fromUtf8("menuDocuments"))
        Main_Formation.setMenuBar(self.menuBar)
        self.actionNouvelle_Formation = QtGui.QAction(Main_Formation)
        self.actionNouvelle_Formation.setObjectName(_fromUtf8("actionNouvelle_Formation"))
        self.actionModifier_Formation = QtGui.QAction(Main_Formation)
        self.actionModifier_Formation.setObjectName(_fromUtf8("actionModifier_Formation"))
        self.actionAttestation_de_presence = QtGui.QAction(Main_Formation)
        self.actionAttestation_de_presence.setObjectName(_fromUtf8("actionAttestation_de_presence"))
        self.actionHabilitations = QtGui.QAction(Main_Formation)
        self.actionHabilitations.setObjectName(_fromUtf8("actionHabilitations"))
        self.menuNouvelle_Cartographie.addAction(self.actionNouvelle_Formation)
        self.menuNouvelle_Cartographie.addAction(self.actionModifier_Formation)
        self.menuDocuments.addAction(self.actionAttestation_de_presence)
        self.menuDocuments.addAction(self.actionHabilitations)
        self.menuBar.addAction(self.menuNouvelle_Cartographie.menuAction())
        self.menuBar.addAction(self.menuDocuments.menuAction())

        self.retranslateUi(Main_Formation)
        QtCore.QMetaObject.connectSlotsByName(Main_Formation)

    def retranslateUi(self, Main_Formation):
        Main_Formation.setWindowTitle(_translate("Main_Formation", "Racapitulatif formations", None))
        self.label_7.setText(_translate("Main_Formation", "Recapitulatif des Formations", None))
        self.tableWidget_recap.setSortingEnabled(True)
        item = self.tableWidget_recap.horizontalHeaderItem(0)
        item.setText(_translate("Main_Formation", "Nom Formation", None))
        item = self.tableWidget_recap.horizontalHeaderItem(1)
        item.setText(_translate("Main_Formation", "Date", None))
        item = self.tableWidget_recap.horizontalHeaderItem(2)
        item.setText(_translate("Main_Formation", "Type de formation", None))
        item = self.tableWidget_recap.horizontalHeaderItem(3)
        item.setText(_translate("Main_Formation", "Domaine", None))
        item = self.tableWidget_recap.horizontalHeaderItem(4)
        item.setText(_translate("Main_Formation", "Plan", None))
        item = self.tableWidget_recap.horizontalHeaderItem(5)
        item.setText(_translate("Main_Formation", "Liste des Participants", None))
        self.menuNouvelle_Cartographie.setTitle(_translate("Main_Formation", "Menu", None))
        self.menuDocuments.setTitle(_translate("Main_Formation", "Documents", None))
        self.actionNouvelle_Formation.setText(_translate("Main_Formation", "Nouvelle Formation", None))
        self.actionModifier_Formation.setText(_translate("Main_Formation", "Modifier", None))
        self.actionAttestation_de_presence.setText(_translate("Main_Formation", "Attestation de presence", None))
        self.actionHabilitations.setText(_translate("Main_Formation", "Habilitations", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Main_Formation = QtGui.QMainWindow()
    ui = Ui_Main_Formation()
    ui.setupUi(Main_Formation)
    Main_Formation.show()
    sys.exit(app.exec_())

