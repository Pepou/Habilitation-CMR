#-*- coding: utf-8 -*-
from PyQt4 import QtGui

import sys
#from GUI.Exploitation_enregistreurs import Exploitation_enregistreurs
#from GUI.connexion2 import Connexion
from GUI.CMR import Gestion_CMR
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.engine import create_engine

from GUI.Formation import Formation


import json

if __name__ == "__main__":
    
    with open("config_bdd.json") as json_file:
        config_bdd = json.load(json_file)       
        namebdd = config_bdd["name_bdd"] #Labo_Metro_Prod"#"Test_carac_generateurs"#"Labo_Metro_Prod"# #
        adressebdd = config_bdd["adresse_bdd"]#"10.42.1.74" #"localhost"  #"10.42.1.74"          
        portbdd = config_bdd["port_bdd"]
    global engine
    engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}".format("FCA", "27.07.80", adressebdd, portbdd, namebdd))
    
    
    app = QtGui.QApplication(sys.argv)
    
#    formation = Formation(engine)
#    formation.show()
    
    myapp = Gestion_CMR(engine)
    myapp.show()    
    
    sys.exit(app.exec_())


    



