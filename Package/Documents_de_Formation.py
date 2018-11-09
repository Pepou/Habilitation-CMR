from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.orm import mapper
#import pandas as pd

from sqlalchemy.ext.automap import automap_base
#from PyQt4.QtGui import QMessageBox
import pendulum
from path import Path
from PyQt4.QtGui import QFileDialog
#import shutil
import win32com.client as win32


class Attestation_formation():
    """"class qui gere la creation des attestation de formation en word"""


    def __init__(self, donnees):
        self.donnees = donnees
        
        self.word = win32.gencache.EnsureDispatch('Word.Application')
        self.word.Visible = False 
        
    def document_presence(self):
        
        chemin_sauvegarde = Path(QFileDialog.getExistingDirectory(None, "Choisir le repertoire de sauvegarde",None
                                                ,
                                                QFileDialog.ShowDirsOnly))
        
        
        if chemin_sauvegarde !="":            
            
            try:
        
                chemin_fichier = Path('AppData/Documents/Attestation de formation.docx').abspath()
                
                for ele in self.donnees["tableau_resultats"]:
                    doc = self.word.Documents.Open(chemin_fichier)
                
                    doc.Bookmarks("Nom_Prenom").Range.Text = ele["nom"].upper() +" " + ele["prenom"].capitalize()
                    
                    doc.Bookmarks("Programme").Range.Text = self.donnees["plan"]
                    doc.Bookmarks("Domaines").Range.Text = self.donnees["domaine"]
                    
                    doc.Bookmarks("Date_Formation").Range.Text = "Le" + " " +self.donnees["date"]
                    
                    sauvegarde_docx = chemin_sauvegarde /f"""{ele["nom"].upper()}_{ele["prenom"].capitalize()}.docx"""
    #                shutil.copy2(chemin_fichier,chemin_sauvegarde )
    
                    if float(ele["note"]) >= 11 :
                        formation ="Acquises"
                        
                    elif 7<= float(ele["note"]) <= 10:
                        formation ="À améliorer"
                        
                    else:
                        formation ="Non acquises"
                        
                    doc.Bookmarks("Resultat").Range.Text = formation
    #                print(sauvegarde_docx)
                    doc.SaveAs(sauvegarde_docx)
            except:
                pass
            finally:
                doc.Close()
        
        self.word.Application.Quit()


class Habilitation():    
    
    def __init__(self, engine):
        
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
        self.FORMATION = Base.classes.GESTION_FORMATION

    def document_habilitation(self):
        """fct qui gere les documents d'habilitation"""
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
    
