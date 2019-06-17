#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Console en python3

#Importations
from datetime import datetime
import tkinter as tki
from subprocess import call as lancerProgramme
from subprocess import Popen
import os

class Console():
    #x-x-x-x-x-x-x-x-x-x Initialisation x-x-x-x-x-x-x-x-x-x
    def __init__(self,master):
        self.root = master
        self.fonction_initialisation_parametres()
        self.fonction_affichage()
        self.fonction_initialisationConsole()
        self.fonction_evenementsTags()

    #x-x-x-x-x-x-x-x-x-x Affichage / Utilitaire x-x-x-x-x-x-x-x-x-x
    def fonction_initialisation_parametres(self):
        self.entreeCouleur = 'orangered'
        self.texteCouleur = 'orangered'
        self.reponseCouleur = 'white'
        self.fondCouleur = "black"
        self.indexLigne = 1
    def fonction_affichage(self):
        # Frame et scrollbar
        self.frameTexte = tki.Frame(self.root, width=600, height=600)
        self.frameTexte.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        self.frameTexte.grid_propagate(False)
        # implement stretchability
        self.frameTexte.grid_rowconfigure(0, weight=1)
        self.frameTexte.grid_columnconfigure(0, weight=1)

        # create a Text widget
        self.txt = tki.Text(self.frameTexte, borderwidth=3, relief="sunken", bg=self.fondCouleur, foreground=self.texteCouleur)
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(self.frameTexte, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
    def fonction_commandes(self):
        self.commande = self.commande.split()

        #Définis le choix de la commande
        if self.commande[0] == 'time' or self.commande[0] == 'date': self.commande_date();
        elif self.commande[0] == 'heure' : self.commande_heure();
        elif self.commande[0] == 'commandes' : self.commande_commandes();
        elif self.commande[0] == 'clear' or self.commande[0] == 'nettoyer': self.commande_nettoyer();
        elif self.commande[0] == 'jour': self.commande_jour();
        elif self.commande[0] == 'nuit': self.commande_nuit();

        #Si la commande n'est pas reconnue
        else:
            self.fonction_ecrireLigne('Commande non reconnue')
            self.fonction_retourCommande()
    def fonction_evenementsTags(self):
        #Evenements
        self.root.bind('<KeyPress-Return>',self.fonction_recuptexteconsole)
        #Gestion des tags
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)
    def fonction_initialisationConsole(self):
        self.fonction_ecrireLigne('Bienvenue dans la console !')
        self.fonction_ecrireLigne('Elle peut exécuter des fonctions simples, possède les modes jour/nuit et une interface dynamique.')
        self.fonction_ecrireLigne("Tapez 'commandes' pour avoir la liste de toutes les commandes avec leur description.")
        self.fonction_ecrireLigne('')
        self.fonction_retourCommande()
    def fonction_recuptexteconsole(self,event):
        #Récupération de la commande
        self.commande = self.txt.get(str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        self.commande = self.commande.replace('$ ','')

        print('indice = ',self.indexLigne, 'et commande = ',self.commande)
        self.txt.tag_add('admin',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        self.indexLigne += 1
        self.fonction_commandes()
    def fonction_retourCommande(self):
        #Retour à l'invite de commande
        self.txt.insert(tki.INSERT,  "$ ")
        self.txt.tag_add('admin',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
    def fonction_ecrireLigne(self,chaine):
        chaine = chaine + "\n"
        self.txt.insert(tki.INSERT, chaine)
        self.txt.tag_add('reponse',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        self.indexLigne += 1



    #Commandes
    def commande_commandes(self):
        #Affichage de toutes les commandes
        self.fonction_ecrireLigne('Voici la liste des commandes possibles :')
        self.fonction_ecrireLigne(" ")
        self.fonction_ecrireLigne("$ commandes     >>>   Liste toutes les commandes et leurs fonctions.")
        self.fonction_ecrireLigne("$ clear         >>>   Nettoie la console.")
        self.fonction_ecrireLigne("$ heure         >>>   Renvoie l'heure actuelle.")
        self.fonction_ecrireLigne("$ date          >>>   Renvoie la date du jour.")
        self.fonction_ecrireLigne("$ jour          >>>   Met la console en mode jour.")
        self.fonction_ecrireLigne("$ nuit          >>>   Met la console en mode nuit.")


        #Retour à l'invite de commande
        self.fonction_retourCommande()
    def commande_nettoyer(self):
        #Nettoyage
        self.indexLigne = 1
        self.txt.delete('1.0', tki.END)

        #Retour à l'invite de commande
        self.fonction_retourCommande()
    def commande_date(self):
        #Affichage de la date locale
        date = datetime.now()
        self.fonction_ecrireLigne("Aujourd'hui on est le {}/{}/{}.".format(str(date.day),str(date.month),str(date.year)))

        #Retour à l'invite de commande
        self.fonction_retourCommande()
    def commande_heure(self):
        #Affichage de l'heure locale
        date = datetime.now()
        self.fonction_ecrireLigne("Il est {}:{}.".format(str(date.hour),str(date.minute)))

        #Retour à l'invite de commande
        self.fonction_retourCommande()
    def commande_jour(self):
        #Mettre la console en mode jour
        self.entreeCouleur = 'orangered'
        self.texteCouleur = 'orangered'
        self.reponseCouleur = 'black'
        self.fondCouleur = 'white'

        #Mise à jour
        self.txt['foreground'] = self.texteCouleur
        self.txt['background'] = self.fondCouleur
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)

        #Message
        self.fonction_ecrireLigne("La console est maintenant en mode jour.")

        #Retour à l'invite de commande
        self.fonction_retourCommande()
    def commande_nuit(self):
        #Mettre la console en mode jour
        self.entreeCouleur = 'orangered'
        self.texteCouleur = 'orangered'
        self.reponseCouleur = 'white'
        self.fondCouleur = 'black'

        #Mise à jour
        self.txt['foreground'] = self.texteCouleur
        self.txt['background'] = self.fondCouleur
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)

        #Message
        self.fonction_ecrireLigne("La console est maintenant en mode nuit.")

        #Retour à l'invite de commande
        self.fonction_retourCommande()






def main():
    root = tki.Tk()
    root.title("Console")
    root.wm_state('zoomed')
    Console(root)
    root.mainloop()
if __name__ == "__main__":
    main()