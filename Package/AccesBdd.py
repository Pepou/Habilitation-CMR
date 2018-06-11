from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.orm import mapper
import pandas as pd
import pendulum
from sqlalchemy.ext.automap import automap_base
from PyQt4.QtGui import QMessageBox
import pendulum




class Bdd_Cmr():
    """classe pour gerer le rapatriement des donnees CMR:
    nbr d'acte ..."""


    def __init__(self, engine):
        
        Base = automap_base()
        self.engine = engine 
        
        # reflect the tables
        Base.prepare(engine, reflect=True)
        
        
        self.CMR = Base.classes.CORRESPONDANTS
        self.CTRL_AFFICHEUR = Base.classes.AFFICHEUR_CONTROLE_ADMINISTRATIF
        self.CARTO = Base.classes.CARTO_ADMINISTRATION


    def recup_prestation(self):
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
        
        dt_carto = pendulum.now('Europe/Paris').subtract(years=3)
        dt_afficheur =pendulum.now('Europe/Paris').subtract(years=1)
        
        result = session.query( self.CMR.NOM,
                                self.CMR.PRENOM, 
                                self.CARTO.DATE_REALISATION,
                                self.CARTO.NUM_RAPPORT,
                                self.CTRL_AFFICHEUR.DATE_CONTROLE,
                                self.CTRL_AFFICHEUR.NUM_DOC                                
                                ).\
                                join(self.CARTO, self.CARTO.ID_OPERATEUR == self.CMR.ID_CMR )\
                                .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
                                .order_by(self.CMR.NOM)\
                                .distinct()\
                                .filter(and_(self.CARTO.DATE_REALISATION>= dt_carto, self.CTRL_AFFICHEUR.DATE_CONTROLE>=dt_afficheur))\
                                .all()

#        for ele in result:
#            for x in ele:
#                print(x[0])
#            print(ele[0])
#            print(ele[1])
        nom_prenom = set([ele[0] +" "+ ele[1] for ele in result])

        
        print(nom_prenom)














