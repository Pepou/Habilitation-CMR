from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.orm import mapper
#import pandas as pd

from sqlalchemy.ext.automap import automap_base
#from PyQt4.QtGui import QMessageBox
import pendulum
from path import Path
from PyQt4.QtGui import QFileDialog
import shutil
import win32com.client as win32
import time
class Bdd_Cmr():
    """classe pour gerer le rapatriement des donnees CMR:
    nbr d'acte ..."""


    def __init__(self, engine):
#        print("couocu")
        Base = automap_base()
        self.engine = engine 
        
        # reflect the tables
        Base.prepare(engine, reflect=True)
        
        
        self.CMR = Base.classes.CORRESPONDANTS
        self.CTRL_AFFICHEUR = Base.classes.AFFICHEUR_CONTROLE_ADMINISTRATIF
        self.CARTO = Base.classes.CARTO_ADMINISTRATION
        self.SITE = Base.classes.CLIENTS
        self.SERVICE = Base.classes.SERVICES_CLIENT
        self.ENT_CLIENT = Base.classes.ENTITE_CLIENT

#        print([c.key for c in self.CMR.__table__.c])
    
    def recup_cmr(self):
#        print("recocuou")
        Session = sessionmaker(bind= self.engine)
        session = Session()
        cmr = session.query(self.CMR)\
                                    .order_by(self.CMR.NOM)\
                                    .all()
                                    
        session.close()
#        print(cmr)
        yield cmr
        
        
    def recherche(self, saisie):
#        print("coucou t dans la place")
#        colonnes = [c for c in self.CMR.__table__.c]
        Session = sessionmaker(bind= self.engine)
        session = Session()
        cmr = session.query(self.CMR) \
                    .filter(or_(func.lower(self.CMR.NOM).contains(func.lower(saisie)), 
                                func.lower(self.CMR.PRENOM).contains(func.lower(saisie))))\
                    .order_by(self.CMR.NOM)\
                    .all()
        session.close()
#        print("coucou t dans la place")
#        print(cmr)
        yield cmr
    
    
    def recup_site(self):
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        clients = session.query(self.SITE.CODE_CLIENT)\
                            .join(self.ENT_CLIENT, self.SITE.ID_ENT_CLIENT == self.ENT_CLIENT.ID_ENT_CLIENT)\
                            .filter(self.ENT_CLIENT.ABREVIATION == "EFS_CPDL")\
                            .all()
                            
        session.close()
        #self.SERVICE.ABREVIATION) \.join(self.SERVICE, self.SITE.ID_CLIENTS == self.SERVICE.ID_CLIENT )\ 
#        print(clients)
#                                       .order_by(self.ADMIN_CARTO.ID_CARTO.desc())\
#                                       .limit(100)
        yield clients
        
    def recupe_services_par_site(self, site):
        Session = sessionmaker(bind= self.engine)
        session = Session()
        services = session.query(self.SERVICE.ABREVIATION)\
                                .join(self.SITE, self.SITE.ID_CLIENTS == self.SERVICE.ID_CLIENT )\
                                .filter(self.SITE.CODE_CLIENT == site)\
                                .all()
                                
        session.close()
#        print(services)
        
        yield services
        
        
    def insertion_new_cmr(self, cmr):
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
        new_cmr = self.CMR(NOM = cmr["nom"], 
                            PRENOM = cmr["prenom"], 
                            SERVICE = cmr["service"], 
                            FONCTION= cmr["fonction"], 
                            SITE= cmr["site"], 
                            COURRIEL = cmr["courriel"], 
                            RESPONSABLE= cmr["responsable"], 
                            ARCHIVAGE = False)
                
        
        session.add(new_cmr)
        session.commit()
        session.close()
        
    def recup_id_cmr(self, nom, prenom):
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        id = session.query(self.CMR.ID_CMR) \
                    .filter(and_(func.lower(self.CMR.NOM)==(func.lower(nom)), 
                                func.lower(self.CMR.PRENOM) == (func.lower(prenom))))\
                    .first()
        session.close()
#        print("coucou t dans la place")
#        print(id)
        yield id[0]
        
    def modif_cmr(self, saisie_cmr):
        print(saisie_cmr)
        Session = sessionmaker(bind= self.engine)
        session = Session()
        cmr_modif = session.query(self.CMR).get(saisie_cmr["id"])
        
        cmr_modif.NOM =saisie_cmr["nom"]
        cmr_modif.PRENOM = saisie_cmr["prenom"]
        cmr_modif.SERVICE= saisie_cmr["service"]
        cmr_modif.FONCTION = saisie_cmr["fonction"]
        cmr_modif.SITE = saisie_cmr["site"]
        cmr_modif.COURRIEL = saisie_cmr["courriel"]
        cmr_modif.RESPONSABLE = saisie_cmr["responsable"]
        cmr_modif.ARCHIVAGE = saisie_cmr["activite"]
        session.flush()
        session.commit()
        session.close()
    
    def recup_prestation(self):      
        
        
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = False
        
        
        chemin_fichier = Path('AppData/Documents/PDL_PIL_SUR_MET_FO_006_V2.docx').abspath()
#        print(chemin_fichier)
#        doc = word.Documents.Open(chemin_fichier)
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
        
        dt_carto = pendulum.now('Europe/Paris').subtract(years=3)
        dt_sat_aft_tev = pendulum.now('Europe/Paris').subtract(years=1)
        dt_afm = pendulum.now('Europe/Paris').subtract(years=3)
        
        
        nom_prenom_cmr = session.query( self.CMR.NOM,self.CMR.PRENOM)\
                                            .order_by(self.CMR.NOM)\
                                            .filter(self.CMR.ARCHIVAGE == False)\
                                            .all()
        

        
#        chemin_sauvegarde = str(QFileDialog.getExistingDirectory(None, "Choisir le repertoire de sauvegarde",
#                                                "y:/1.METROLOGIE/0.ARCHIVES ETALONNAGE-VERIFICATIONS/3-CARTOS-SIMULATION/",
#                                                QFileDialog.ShowDirsOnly))
        
        
        chemin_sauvegarde = Path(QFileDialog.getExistingDirectory(None, "Choisir le repertoire de sauvegarde",None
                                                ,
                                                QFileDialog.ShowDirsOnly))
        
        
        if chemin_sauvegarde !="":            
        
#            nom = file +"/"+ sauvegarde["administratif"]["num_rapport"]
            
            
            for nom_prenom in nom_prenom_cmr:
    #            presta_par_cmr = []
                doc = word.Documents.Open(chemin_fichier)
                
                afficheur_sat_tev_aft = session.query( self.CMR.NOM,
                                    self.CMR.PRENOM, 
                                    self.CTRL_AFFICHEUR.DATE_CONTROLE,
                                    self.CTRL_AFFICHEUR.NUM_DOC                                
                                    )\
                                    .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
                                    .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE >= dt_sat_aft_tev,  
                                                    self.CMR.ARCHIVAGE == False, 
                                                        or_(self.CTRL_AFFICHEUR.NUM_DOC.contains("%SAT%"),
                                                            self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFT%" ), 
                                                            self.CTRL_AFFICHEUR.NUM_DOC.contains("%TEV%")), 
                                                        and_(self.CMR.NOM == nom_prenom[0],self.CMR.PRENOM == nom_prenom[1])))\
                                    .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
                                    .first()
                if not afficheur_sat_tev_aft:
                    afficheur_sat_tev_aft = (None, None, None, None)
                    
                                    
                afficheur_afm = session.query( self.CMR.NOM,
                                    self.CMR.PRENOM, 
                                    self.CTRL_AFFICHEUR.DATE_CONTROLE,
                                    self.CTRL_AFFICHEUR.NUM_DOC                                
                                    )\
                                    .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
                                    .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE>= dt_afm,  
                                                    self.CMR.ARCHIVAGE == False, 
                                                    self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFM%"), \
                                                    and_(self.CMR.NOM == nom_prenom[0],self.CMR.PRENOM == nom_prenom[1])))\
                                    .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
                                    .first()
                if not afficheur_afm:
                    afficheur_afm = (None, None, None, None)
                                    
                afficheur_afv = session.query( self.CMR.NOM,
                                    self.CMR.PRENOM, 
                                    self.CTRL_AFFICHEUR.DATE_CONTROLE,
                                    self.CTRL_AFFICHEUR.NUM_DOC                                
                                    )\
                                    .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
                                    .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE>= dt_afm,  
                                                    self.CMR.ARCHIVAGE == False, 
                                                    self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFV%"), \
                                                    and_(self.CMR.NOM == nom_prenom[0],self.CMR.PRENOM == nom_prenom[1])))\
                                    .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
                                    .first()
                                    
                if not afficheur_afv:
                    afficheur_afv = (None, None, None, None)

                carto = session.query( self.CMR.NOM,
                                    self.CMR.PRENOM, 
                                    self.CARTO.DATE_REALISATION,
                                    self.CARTO.NUM_RAPPORT)\
                                    .join(self.CARTO, self.CARTO.ID_OPERATEUR == self.CMR.ID_CMR )\
                                    .filter(and_(self.CARTO.DATE_REALISATION>= dt_carto, 
                                                self.CMR.ARCHIVAGE == False), 
                                                and_(self.CMR.NOM == nom_prenom[0],self.CMR.PRENOM == nom_prenom[1]))\
                                    .order_by(self.CARTO.ID_CARTO.desc())\
                                    .first()
                if not carto:
                    carto = (None, None, None, None)

                
                
                
                
                doc.Bookmarks("NOM").Range.Text = nom_prenom[0].upper()
                doc.Bookmarks("PRENOM").Range.Text = nom_prenom[1].capitalize()
                doc.Bookmarks("DATE").Range.Text = pendulum.now().format('DD/MM/YYYY',formatter='alternative')
                
#                print(f"{nom_prenom[0]} {nom_prenom[1]} {afficheur_afm[3]} {afficheur_afm[2]}\
#                        {afficheur_afv[3]}\
#                        {afficheur_afv[2]}\
#                        {afficheur_sat_tev_aft[3]}\
#                        {afficheur_afv[2]}\
#                        {afficheur_sat_tev_aft[3]}\
#                        {afficheur_sat_tev_aft[2]}\
#                        {carto[3]}\
#                    {carto[2]}")
                try:
                    if afficheur_afm[3]:#"n_ce_temps"
                        doc.Bookmarks("TEMPS_A").Range.Text = afficheur_afm[3] +" du "+afficheur_afm[2].strftime('%d/%m/%Y')               
                    else:
                        doc.Bookmarks("TEMPS_NA").Range.Text = "Na"
                except:
                    print("TEMPS_NA")
                    pass
                    
                
                try:
                    if afficheur_afv[3]:#"n_ce_temps"
                        doc.Bookmarks("VITESSE_A").Range.Text = afficheur_afv[3] +" du "+afficheur_afv[2].strftime('%d/%m/%Y')                
                    else:
                        doc.Bookmarks("VITESSE_NA").Range.Text = "Na"
                except:
                    print("VITESSE_A")
                    pass
                    
                try:
                    if afficheur_sat_tev_aft[3]:#"n_ce_temps"
                        doc.Bookmarks("TEMOIN_A").Range.Text = afficheur_sat_tev_aft[3] +" du "+afficheur_sat_tev_aft[2].strftime('%d/%m/%Y')                
                    else:
                        doc.Bookmarks("TEMOIN_NA").Range.Text = "Na"
                except:
                    print("TEMOIN_A")
                    pass
                try:
                    if carto[3]:#"n_ce_temps"
                        doc.Bookmarks("CARTO_A").Range.Text = carto[3] +" du "+carto[2].strftime('%d/%m/%Y')                
                    else:
                        doc.Bookmarks("CARTO_NA").Range.Text = "Na"
                
                except:
                    print("CARTO_A")
                    pass
                    
                sauvegarde_docx = chemin_sauvegarde /f"{nom_prenom[0].upper()}_{nom_prenom[1].capitalize()}.docx"
#                shutil.copy2(chemin_fichier,chemin_sauvegarde )
                print(sauvegarde_docx)
                doc.SaveAs(sauvegarde_docx)
                doc.Close()
        
        word.Application.Quit()
        session.close()
#                time.sleep(15)
#                
#            print(list_presta)

            
#        print(f"carto : {nom_prenom_cmr}")
#        print(f"afficheur {[list(item) for item in set(tuple(row) for row in afficheur_sat_tev_aft)]}")










        
#        carto = session.query( self.CMR.NOM,
#                                self.CMR.PRENOM, 
#                                self.CARTO.DATE_REALISATION,
#                                self.CARTO.NUM_RAPPORT)\
#                                .join(self.CARTO, self.CARTO.ID_OPERATEUR == self.CMR.ID_CMR )\
#                                .filter(and_(self.CARTO.DATE_REALISATION>= dt_carto, 
#                                            self.CMR.ARCHIVAGE == False))\
#                                .order_by(self.CARTO.ID_CARTO.desc())\
#                                .distinct()\
#                                .all()
#        
#        
#        
#        
#        afficheur_sat_tev_aft = session.query( self.CMR.NOM,
#                                self.CMR.PRENOM, 
#                                self.CTRL_AFFICHEUR.DATE_CONTROLE,
#                                self.CTRL_AFFICHEUR.NUM_DOC                                
#                                )\
#                                .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
#                                .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE >= dt_sat_aft_tev,  
#                                                self.CMR.ARCHIVAGE == False, 
#                                                or_(self.CTRL_AFFICHEUR.NUM_DOC.contains("%SAT%"),
#                                                    self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFT%" ), 
#                                                    self.CTRL_AFFICHEUR.NUM_DOC.contains("%TEV%"))))\
#                                .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
#                                .distinct()\
#                                .all()
#
#        afficheur_afv = session.query(self.CMR.NOM,
#                                self.CMR.PRENOM, 
#                                self.CTRL_AFFICHEUR.DATE_CONTROLE,
#                                self.CTRL_AFFICHEUR.NUM_DOC                                
#                                )\
#                                .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
#                                .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE >= dt_afm,  
#                                                self.CMR.ARCHIVAGE == False, 
#                                                self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFV%")))\
#                                .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
#                                .distinct()\
#                                .all()
#                                
#                                
#                                
#        afficheur_afm = session.query( self.CMR.NOM,
#                                self.CMR.PRENOM, 
#                                self.CTRL_AFFICHEUR.DATE_CONTROLE,
#                                self.CTRL_AFFICHEUR.NUM_DOC                                
#                                )\
#                                .join(self.CTRL_AFFICHEUR, self.CTRL_AFFICHEUR.TECHNICIEN == self.CMR.ID_CMR )\
#                                .filter(and_(self.CTRL_AFFICHEUR.DATE_CONTROLE>= dt_afm,  
#                                                self.CMR.ARCHIVAGE == False, 
#                                                self.CTRL_AFFICHEUR.NUM_DOC.contains("%AFM%")))\
#                                .order_by(self.CTRL_AFFICHEUR.ID_AFFICHEUR_ADMINISTRATIF.desc())\
#                                .distinct()\
#                                .all()
        



