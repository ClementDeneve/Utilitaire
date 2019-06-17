#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Console en python3

#Importations
import tkinter as tki
from methodes import ListeMethodes
from utilitaires import ListeFonctions
from parametres import Configuration
from test import Tests


class Console(ListeMethodes,ListeFonctions,Configuration,Tests):
    #x-x-x-x-x-x-x-x-x-x Initialisation x-x-x-x-x-x-x-x-x-x
    def __init__(self,master):
        self.root = master
        self.fonction_initialisation_parametres()
        self.fonction_affichage()
        self.fonction_initialisationConsole()
        self.fonction_evenementsTags()

    #x-x-x-x-x-x-x-x-x-x Redirection commandes disponibles x-x-x-x-x-x-x-x-x-x
    def fonction_commandes(self):
        self.commande = self.commande.split()

        #Définis le choix de la commande
        if   self.commande[0] == 'date':            self.commande_date();
        elif self.commande[0] == 'heure' :          self.commande_heure();
        elif self.commande[0] == 'commandes':       self.commande_commandes();
        elif self.commande[0] == 'test' :           self.commande_test();
        elif self.commande[0] == 'clear':           self.commande_nettoyer(0);
        elif self.commande[0] == 'jour':            self.commande_jour();
        elif self.commande[0] == 'nuit':            self.commande_nuit();
        elif self.commande[0] == 'bin':             self.commande_bin();
        elif self.commande[0] == 'hex':             self.commande_hex();
        elif self.commande[0] == 'exec':            self.commande_exec();
        elif self.commande[0] == 'calcul':          self.commande_calcul();
        elif self.commande[0] == 'meteo':           self.commande_meteo();
        elif self.commande[0] == 'input':           self.commande_input();
        elif self.commande[0] == 'cd':              self.commande_cd();
        elif self.commande[0] == 'pwd':             self.commande_pwd();
        elif self.commande[0] == 'investloc':       self.commande_investissement_locatif();
        elif self.commande[0] == 'anagrammes':      self.commande_anagrammes();
        elif self.commande[0] == 'pi':              self.commande_pi();
        elif self.commande[0] == 'definition':      self.commande_definition();
        elif self.commande[0] == 'anniv':           self.commande_anniversaires();
        elif self.commande[0] == 'anniv_add':       self.commande_anniv_add();
        elif self.commande[0] == 'anniv_remove':    self.commande_anniv_remove();
        elif self.commande[0] == 'print':           self.commande_print()
        elif self.commande[0] == 'rr_party':        self.commande_rr_party()
        #Si la commande n'est pas reconnue
        else:
            self.fonction_ecrireLigne('Commande non reconnue')
            self.fonction_retourCommande()

    #Description des commandes utilisables
    def commande_commandes(self):
        #Lecture du fichier de description de commandes
        fichier = open("description_commandes.txt", "r")
        texte = fichier.readlines()

        #Boucle sur les lignes du fichier
        for i in texte:
            self.fonction_ecrireLigne(i[:-1])

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