# -*- coding: utf-8 -*-

"""
Module implementing Habilitation_CMR.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow

from .Ui_CMR import Ui_Habilitation_CMR

from Package.AccesBdd import Bdd_Cmr

class Habilitation_CMR(QMainWindow, Ui_Habilitation_CMR):
    """
    Class documentation goes here.
    """
    def __init__(self, engine , parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        
        bdd = Bdd_Cmr(engine)
        bdd.recup_prestation()
        
    @pyqtSlot(str)
    def on_lineEdit_cmr_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
