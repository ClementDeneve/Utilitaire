#Importations
import tkinter as tki
from datetime import datetime

class Configuration():

    #Message à l'arrivée dans la console
    def fonction_initialisationConsole(self):
        self.fonction_ecrireLigne('Bienvenue dans la console !')
        self.fonction_ecrireLigne('On est le '+ self.date)
        self.fonction_ecrireLigne('Elle peut exécuter des fonctions simples, possède les modes jour/nuit et une interface dynamique.')
        self.fonction_ecrireLigne("Tapez 'commandes' pour avoir la liste de toutes les commandes avec leur description.")
        self.fonction_ecrireLigne('')

        #Affichage des anniversaires
        for i in range(len(self.liste_anniversaire)):
            if self.date[:-4] == self.liste_anniversaire[i][2][:-4]:
                self.fonction_ecrireLigne("!!!!!  ALERTE ANNIVERSAIRE  !!!!!")
                self.fonction_ecrireLigne("Aujourd'hui c'est l'anniversaire de " + self.liste_anniversaire[i][0]+' '+self.liste_anniversaire[i][1]+' !!!!!!')
                age = int(self.date[-4:]) - int(self.liste_anniversaire[i][2][-4:])
                self.fonction_ecrireLigne(str(age)+ " ans ça se fête ! ")

        #Retour commande
        self.fonction_retourCommande()


    #Définition de tous les paramètres initiaux
    def fonction_initialisation_parametres(self):

        #Couleurs
        self.entreeCouleur = 'orangered'                    #Couleur du tag 'admin'
        self.texteCouleur = 'orangered'                     #Couleur du texte de base
        self.reponseCouleur = 'white'                       #Couleur de la réponse ordinateur
        self.fondCouleur = "black"                          #Couleur du fond de la console
        self.insertbg = 'white'                             #Couleur du curseur
        self.couleurInput = 'green'                         #Couleur des saisies
        self.etatLumiere = 'nuit'

        #Indices
        self.indexLigne = 1                                 #Indice qui repère le numéro de ligne

        #Autres
        self.mode = 'console'                               #Mode de l'application
        self.input = tki.StringVar()                        #Chaine dans laquelle est stockée l'input utilisateur
        self.repertoireCourant = 'C:/Users/cleme/Desktop/Python/Projets/Conspy'
        date = datetime.now()

        if len(str(date.day)) == 1:
            jour = '0'+str(date.day)
        else:
            jour = str(date.day)

        if len(str(date.month)) == 1:
            mois = '0'+str(date.month)
        else:
            mois = str(date.month)
        self.date = "{}/{}/{}".format(jour,mois,str(date.year))


        #Récupération des anniversaires
        import sqlite3
        fichierDonnees = "C:/Users/cleme/Desktop/Informatique/Projets - Python/Conspy/data/anniv.sq3"

        #Connection
        conn =sqlite3.connect(fichierDonnees) 

        #Curseur de sécurité
        cur =conn.cursor()

        #Récupération des données
        cur.execute("SELECT * FROM anniversaires")
        self.liste_anniversaire = list(cur)


        #Validation
        conn.commit()

        #Fermeture des connections
        cur.close()
        conn.close()