from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.orm import mapper
#import pandas as pd

from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.dialects.postgres import JSON
from sqlalchemy.sql.expression import cast
#from PyQt4.QtGui import QMessageBox
import pendulum
from path import Path
from PyQt4.QtGui import QFileDialog
#import shutil
import win32com.client as win32
#import time
import json
from sqlalchemy.dialects.postgresql import JSON, ARRAY

class Bdd_Cmr():    
    
    """classe pour gerer le rapatriement des donnees CMR:
    nbr d'acte ..."""


    def __init__(self, engine):
#        print("couocu")
        metadata = MetaData() 
        metadata.reflect(engine, only=['CORRESPONDANTS', 'AFFICHEUR_CONTROLE_ADMINISTRATIF', 
                                        'CARTO_ADMINISTRATION', 'CLIENTS', 
                                        'SERVICES_CLIENT', 'ENTITE_CLIENT', 
                                        'GESTION_FORMATION'])
        
        Base = automap_base(metadata=metadata)
        self.engine = engine 
        
        # reflect the tables
        Base.prepare()
        
        
        self.CMR = Base.classes.CORRESPONDANTS
        self.CTRL_AFFICHEUR = Base.classes.AFFICHEUR_CONTROLE_ADMINISTRATIF
        self.CARTO = Base.classes.CARTO_ADMINISTRATION
        self.SITE = Base.classes.CLIENTS
        self.SERVICE = Base.classes.SERVICES_CLIENT
        self.ENT_CLIENT = Base.classes.ENTITE_CLIENT
        self.FORMATION = Base.classes.GESTION_FORMATION

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
        
#    def recup_id_cmr(self, nom, prenom):
##        print("recocuou")
#        Session = sessionmaker(bind= self.engine)
#        session = Session()
#        cmr = session.query(self.CMR.ID_CMR)\
#                                    .filter(and_(func.lower(self.CMR.NOM) == (func.lower(nom)), 
#                                                func.lower(self.CMR.PRENOM) == (func.lower(prenom))))\
#                                    .order_by(self.CMR.NOM)\
#                                    .first()
#                                    
#        session.close()
##        print(cmr)
#        yield cmr   
    
    
    def recup_cmr_en_activite(self):
#        print("recocuou")
        Session = sessionmaker(bind= self.engine)
        session = Session()
        cmr = session.query(self.CMR)\
                                    .filter(self.CMR.ARCHIVAGE != True)\
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
        
#        print(cmr)
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
        return id[0]
        
    def modif_cmr(self, saisie_cmr):
#        print(saisie_cmr)
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
    
    
    def insertion_formation(self, donnees):
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        try:
            new_formation = self.FORMATION(NOM_FORMATION = donnees["nom_formation"] , 
                                DATE_FORMATION = donnees["date"], 
                                TYPE_FORMATION = donnees["type_formation"], 
                                DOMAINE= donnees["domaine"], 
                                PLAN= donnees["plan"], 
                                LIST_PARTICIPANTS = cast(donnees["participants"], ARRAY(JSON)) 
                                )
                    
            
            session.add(new_formation)
            session.commit()
        
        except Exception as e:
                print(e)
                session.rollback()
#                
        finally:
                session.close()
        
        
        
        
    
    def modif_formation(self, id_formation_a_modif, donnees):
        """fct pour modif une formation"""
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
#        try:
        formation_a_modif = session.query(self.FORMATION).get(id_formation_a_modif)
        
        formation_a_modif.NOM_FORMATION = donnees["nom_formation"]
        formation_a_modif.DATE_FORMATION = donnees["date"]
        formation_a_modif.TYPE_FORMATION = donnees["type_formation"]
        formation_a_modif.DOMAINE = donnees["domaine"]
        formation_a_modif.PLAN = donnees["plan"]
        formation_a_modif.LIST_PARTICIPANTS = cast(donnees["participants"], ARRAY(JSON))
        session.flush()
        session.commit()
            
#        except Exception as e:
#                print(e)
#                session.rollback()
##                
#        finally:
#                session.close()
            
    
    def recup_formation(self):
        Session = sessionmaker(bind= self.engine)
        session = Session()
        formations = session.query(self.FORMATION) \
                    .order_by(self.FORMATION.ID)\
                    .all()
        
        
        
        yield formations
        session.close()
        
    def recup_formation_particuliere(self, nom, date, domaine, type_formation):
        """fct qui va chercher dans la base une formation en fct du nom date et domaine"""
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        formation = session.query(self.FORMATION) \
                    .filter(and_(self.FORMATION.NOM_FORMATION == nom, self.FORMATION.DATE_FORMATION == date, 
                                    self.FORMATION.DOMAINE == domaine, self.FORMATION.TYPE_FORMATION == type_formation))\
                    .first()
        
        return formation
        session.close()
#        print(formation.NOM_FORMATION)
    
    def recup_prestation(self):      
        
        
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = False
        
        
        chemin_fichier = Path('AppData/Documents/PDL_PIL_SUR_MET_FO_006_V2.docx').abspath()
#        print(chemin_fichier)
#        doc = word.Documents.Open(chemin_fichier)
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
#        dt_formation = pendulum.now('Europe/Paris').subtract(years=1)
#        date_now = pendulum.now('Europe/Paris')
#        print(dt_formation)
#        print(dt_formation.year)
        
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
            formation =session.query( self.FORMATION.ID, 
                                        self.FORMATION.LIST_PARTICIPANTS, 
                                        self.FORMATION.DOMAINE, 
                                        self.FORMATION.DATE_FORMATION, 
                                        self.FORMATION.TYPE_FORMATION)\
                                        .filter(and_(self.FORMATION.DATE_FORMATION >= (pendulum.datetime(pendulum.now('Europe/Paris').subtract(years=1).year, 1, 1)
), 
                                                      self.FORMATION.DATE_FORMATION <= pendulum.now('Europe/Paris') )).all()

            
            for nom_prenom in nom_prenom_cmr:
#                print(nom_prenom)
    #            presta_par_cmr = []
                
                doc = word.Documents.Open(chemin_fichier)
    
                for ele in formation:
#                    print(ele[1])
                    for participant in ele[1]:                        
                        participan_dict = json.loads(participant)
                        
                        if participan_dict['nom'] == nom_prenom[0] and participan_dict['prenom'] == nom_prenom[1]:
                           
                           
                           ####rajouter ici test sur initiale ou continue:
                            type_formation = ele[4]
                            if type_formation == "Continue":                           
                                if (participan_dict['resultat'] == "Acquises" 
                                            or participan_dict['resultat'] == "Acquise"
                                            or participan_dict['resultat'] == "À améliorer") :
                                    
                                
                                    for domaine in ele[2]:
                                        if domaine == "TEMPÉRATURE":                                
                                            if participan_dict['resultat'] == "Acquises" or participan_dict['resultat'] == "Acquise":
                                                doc.Bookmarks("FORM_CARTO_A").Range.Text = ele[3].strftime("%d-%m-%Y")
                                                doc.Bookmarks("FORM_TEMP_A").Range.Text = ele[3].strftime("%d-%m-%Y")
                                            else:
                                                doc.Bookmarks("FORM_CARTO_AA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                                doc.Bookmarks("FORM_TEMP_AA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                                
                                        elif domaine == "MASSE" or domaine == "ACCÉLÉROMÈTRIE" or domaine == "TEMPS":
                                            if participan_dict['resultat'] == "Acquises" or participan_dict['resultat'] == "Acquise":
                                                doc.Bookmarks("FORM_VIT_TPS_MASSE_A").Range.Text = ele[3].strftime("%d-%m-%Y")                                        
                                            else:
                                                doc.Bookmarks("FORM_VIT_TPS_MASSE_AA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                                                                
                                        elif domaine == "PIPETTES":
                                            if participan_dict['resultat'] == "Acquises" or participan_dict['resultat'] == "Acquise":
                                                doc.Bookmarks("FORM_PIPETTE_A").Range.Text = ele[3].strftime("%d-%m-%Y")                                        
                                            else:
                                                doc.Bookmarks("FORM_PIPETTE_AA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                                
        #                                doc.Bookmarks("NOM").Range.Text
                                
    
                                elif (participan_dict['nom'] == nom_prenom[0] 
                                        and participan_dict['prenom'] == nom_prenom[1]
                                        and (participan_dict['resultat'] == "Non acquise")):
                                    for domaine in ele[2]:
                                        if domaine == "TEMPÉRATURE": 
                                            doc.Bookmarks("FORM_CARTO_NA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                            doc.Bookmarks("FORM_TEMP_NA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                        
                                        elif domaine == "MASSE" or domaine == "ACCÉLÉROMÈTRIE" or domaine == "TEMPS":                                    
                                            doc.Bookmarks("FORM_VIT_TPS_MASSE_NA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                        
                                        elif domaine == "PIPETTES":
                                            doc.Bookmarks("FORM_PIPETTE_NA").Range.Text = ele[3].strftime("%d-%m-%Y")
                            else: #formation initiale
                                if (participan_dict['resultat'] == "Acquises" 
                                            or participan_dict['resultat'] == "Acquise"):
                                            doc.Bookmarks("FORM_INIT_A").Range.Text = ele[3].strftime("%d-%m-%Y")
                                
                                elif (participan_dict['resultat'] == """À améliorer"""):                                            
                                            doc.Bookmarks("FORM_INIT_AA").Range.Text = ele[3].strftime("%d-%m-%Y")
                                            
                                elif participan_dict['resultat'] == "Non acquise":
                                    doc.Bookmarks("FORM_INIT_NA").Range.Text = ele[3].strftime("%d-%m-%Y")
                            
                            
                        else:
                            pass
                
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
#                print(sauvegarde_docx)
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
        

class Insertion_Domaine():
    
    def __init__(self, engine):
#        print("couocu")

        metadata = MetaData() 
        metadata.reflect(engine, only=['DOMAINE_MESURE'])
        Base = automap_base(metadata=metadata)
#        Base = automap_base()
        self.engine = engine 
        
        # reflect the tables
        Base.prepare(engine, reflect=True)        
        
        self.DOMAINE = Base.classes.DOMAINE_MESURE
        
        
    def insertion_table(self):
        

        Session = sessionmaker(bind= self.engine)
        session = Session()
        
        
        accelerometrie = {"domaine":"ACCÉLÉROMÈTRIE", 
                            "famille":[{"FAMILLE":"ANÉMOMÈTRE", 
                                        "DESIGNATION":[{"NOM":"chaine de mesure de la vitesse de l'air".upper(),
                                                        "TYPE":["/","hélice".upper(),"fil chaud".upper(),"hermétique".upper()]}]},
                                        
                                        
                                        ]}
                                        
        humidite= {"domaine":"HYGROMÈTRIE", 
                            "famille":[{"FAMILLE":"HYGROMÈTRE", 
                                        "DESIGNATION":[{"NOM":"chaine de mesure d'humidité".upper(),
                                                        "TYPE":["/","resistif".upper(), "capacitif".upper(), "cheveux".upper()]}, 
                                                        {"NOM":"SONDE D'HYGROMÉTRIE".upper(),
                                                        "TYPE":["/","resistif".upper(), "capacitif".upper(), "cheveux".upper()]}                                                   
                                                                                                               
                                                        
                                                        ]}]}
                                                        
                                                        
                                                        
                        
                                                        
        masse= {"domaine":"MASSE", 
                            "famille":[{"FAMILLE":"BALANCE / SYST PESEE", 
                                        "DESIGNATION":[{"NOM":"balance".upper(),
                                                        "TYPE":["/","Compensation électromagnétique des forces".upper(), "Jauge de contrainte".upper()]}]}, 
                                        
                                        {"FAMILLE":"POIDS ETALON", 
                                        "DESIGNATION":[{"NOM":"POIDS".upper(),
                                                        "TYPE":["/","OIML R 111".upper()]}]}, 
                                                        
                                        {"FAMILLE":"POIDS DE TRAVAIL", 
                                        "DESIGNATION":[{"NOM":"POIDS".upper(),
                                                        "TYPE":["/","OIML R 111".upper()]}]}, 
                                                        
                                        {"FAMILLE":"MASSE ETALON", 
                                        "DESIGNATION":[{"NOM":"masse etalon".upper(),
                                                        "TYPE":["/","OIML R 111".upper()]}]}, 
                                                        
                                        {"FAMILLE":"MASSE DE TRAVAIL", 
                                        "DESIGNATION":[{"NOM":"masse de travail".upper(),
                                                        "TYPE":["/","OIML R 111".upper()]}]}                                
                                                        
                                                        
                                                        
                                    ]}                                
        
        
        
        pression= {"domaine":"PRESSION", 
                            "famille":[{"FAMILLE":"MESURE DE PRESSION", 
                                        "DESIGNATION":[{"NOM":"BAROMÈTRE".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}, 
                                                        
                                                        {"NOM":"manometre".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}], } 
                                                        
                                                                     
                                                        
                                    ]}
        
        temps_frequence= {"domaine":"TEMPS-FRÉQUENCE", 
                            "famille":[{"FAMILLE":"MESURE DE TEMPS", 
                                        "DESIGNATION":[ {"NOM":"CHRONOMÈTRE/MINUTERIE DE TRAVAIL".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]},                                                         
                                                        
                                                        {"NOM":"AFFICHEUR DE TEMPS".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}                                                         
                                                        
                                                        ]}, 
                                                        
                                        {"FAMILLE":"MESURE DE FREQUENCE", 
                                        "DESIGNATION":[{"NOM":"TACHYMETRES".upper(),
                                                        "TYPE":["/","OPTIQUE".upper(),"mécanique".upper(), "courants de Foucault".upper()]}, 

                                                        {"NOM":"AFFICHEUR DE TEMPS".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}, 
                                                        
                                                        {"NOM":"AFFICHEUR DE VITESSE".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}, 
                                                        
                                                        {"NOM":"CENTRI GRDE CAPACITE".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]},
                                                        
                                                        {"NOM":"CENTRI MOY CAPACITE".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}, 
                                                        
                                                        {"NOM":"ULTRA-CENTRIFUGEUSE".upper(),
                                                        "TYPE":["/","numerique".upper(),"analogique".upper()]}
                                                        
                                                        ]}
             
                                    ]}
        
        temperature = {"domaine":"TEMPÉRATURE", 
                            "famille":[{"FAMILLE":"MESURE POLYVAL (T°C)", 
                                        "DESIGNATION":[{"NOM":"AFFICHEUR DE TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "numerique".upper()]}, 
                                                        
                                                        {"NOM":"SONDE ALARME TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "numerique".upper()]}, 
                                                        
                                                        {"NOM":"SONDE ALARME TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "numerique".upper()]}, 
                                                        
                                                        {"NOM":"TÉMOIN D'ENVIRONNEMENT".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "numerique".upper()]}, 

                                                        {"NOM":"CENTRALE DE TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "Thermocouple".upper()]}, 
                                                        
                                                        {"NOM":"CHAÎNE DE MESURE DE TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper()]}, 
                                                        
                                                        {"NOM":"SONDE DE TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "Thermocouple".upper()]}, 
                                                        

                                                        {"NOM":"ENREGISTREUR DE TEMPÉRATURE".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "Thermocouple".upper()]}, 
                                                        
                                                        {"NOM":"ETALON".upper(),
                                                        "TYPE":["/","Thermistance".upper(),"PT100".upper(), "PT1000".upper(), "Thermocouple".upper()]}
                                                        ]}, 
                                                        
                                        
                                        {"FAMILLE":"Générateur".upper(), 
                                        "DESIGNATION":[{"NOM":"BAIN D'ETALONNAGE".upper(),
                                                        "TYPE":["/","à remous".upper(),"à débordement".upper()]}, 
                                                        
                                                        {"NOM":"BAIN DE GLACE FONDANTE".upper(),
                                                        "TYPE":["/","numerique".upper()]},
                                                        
                                                        {"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/","TEMPÉRATURE".upper(),"TEMPÉRATURE-humidité".upper(), "humidité".upper()]},
                                                        
                                                        {"NOM":"FOUR".upper(),
                                                        "TYPE":["/", "PELTIER"]}
                                                        
                                                        ]}, 
                                         
                                        {"FAMILLE":"AUTOCLAVE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]},
                                                       
                                        {"FAMILLE":"BAINS-MARIE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"CHAMBRE FROIDE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"CONSERVAT. PLAQUETTE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"DECONGELATEURS".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"ENCEINTE T°C NEGATIV".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"ENCEINTE T°C POSITIV".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"ETUVES - INCUBATEURS".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"FOUR".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                        
                                        {"FAMILLE":"MATERIEL CRYOGENIQUE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]},

                                        {"FAMILLE":"REFRIGERAT. DOMESTIQ".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}, 
                                                        
                                        {"FAMILLE":"TABLE REFRIGEREE".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]},
                                                       
                                        {"FAMILLE":"THERMOCYCLEUR".upper(), 
                                        "DESIGNATION":[{"NOM":"ENCEINTE CLIMATIQUE".upper(),
                                                        "TYPE":["/"]} ]}
                                        
                                    ]}
        
        
        
        for ele in [accelerometrie, humidite, masse, pression, temps_frequence, temperature]:
        
            new_domaine = self.DOMAINE(DOMAINE = ele["domaine"] , 
                                OPTIONS=cast(ele["famille"], ARRAY(JSON)) 
                                )
            
            
            session.add(new_domaine)
            session.commit()
        session.close()
        
        
    def recuperation_domaine(self):
        
        Session = sessionmaker(bind= self.engine)
        session = Session()
        
        
        
        domaine = session.query(self.DOMAINE.DOMAINE)\
                                    .order_by(self.DOMAINE.DOMAINE)\
                                    .all()
                                    
        session.close()
        return [x[0]for x in domaine]
        
        
        
        
        
        
        
        

