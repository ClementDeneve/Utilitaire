'''
Auteur : Clément Denève
Fonction : Donner le code couleur d'une résistance 
'''

## Importations

from tkinter import *
from math import log10   # logarithmes en base 10

## Définition des classes

class Application:
    
    #Fonction d'initialisation de l'application
    def __init__(self):
        
        #Création de la fenêtre
        self.root =Tk()
        #Titre
        self.root.title('Code des couleurs')
        #Dessin de la résistance
        self.dessineResistance()
        #Zone de texte
        Label(self.root,text ="Entrez la valeur de la résistance, en ohms :").grid(row =2)
        #Bouton montrer placé ligne 3 à gauche
        Button(self.root, text ='Montrer',command =self.changeCouleurs).grid(row =3, sticky = W)
        #Bouton quitter placé ligne 3 à droite
        Button(self.root, text ='Quitter',command =self.root.destroy).grid(row =3, sticky = E)
        #Saisie de la valeur de la résistance placé ligne 3 au centre (pas d'attribut)
        self.entree = Entry(self.root, width =14)
        self.entree.grid(row =3)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.cc = ['black','brown','red','orange','yellow','green','blue','purple','grey','white']
        #Boucle principale de la fenêtre
        self.root.mainloop()

    #Dessin de la résistance
    def dessineResistance(self):
        #Création du canvas
        self.can = Canvas(self.root, width=250, height =100, bg ='ivory')
        #Placement du canvas
        self.can.grid(row =1, pady =5, padx =5)
        #Création du fil
        self.can.create_line(10, 50, 240, 50, width =5) 
        #Création du rectangle de la résistance
        self.can.create_rectangle(65, 30, 185, 70, fill ='light grey', width =2)
        # Dessin des trois lignes colorées (noires au départ) :
        self.ligne = []
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x, 30, x+12, 70, fill='black', width=0))

    #Méthode d'affichage des couleurs en fonction de l'entrée
    def changeCouleurs(self):
        #Obtenir la valeur rentrée par l'utilisateur (get() renvoie une chaîne
        self.v1ch = self.entree.get()
        try:
            v = float(self.v1ch)          # conversion en valeur numérique
        except:
            err =1                        # erreur : entrée non numérique
        else:
            err =0
        if err ==1 or v < 10 or v > 1e11 :
            self.signaleErreur()          # entrée incorrecte ou hors limites
        else:
            li =[0]*3                     # liste des 3 codes à afficher
            logv = int(log10(v))          # partie entière du logarithme
            ordgr = 10**logv              # ordre de grandeur
            #Extraction du premier chiffre significatif :
            li[0] = int(v/ordgr)          # partie entière
            decim = v/ordgr - li[0]       # partie décimale
            #Extraction du second chiffre significatif :
            li[1] = int(decim*10 +.5)     # +.5 pour arrondir correctement
            #Nombre de zéros à accoler aux 2 chiffres significatifs :
            li[2] = logv -1
            #Coloration des 3 lignes :
            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]])

    def signaleErreur(self):
        #Colore le background pour indiquer l'erreur
        self.entree.configure(bg ='red')  
        #Efface après une seconde
        self.root.after(1000, self.videEntree) 

    def videEntree(self):
        #Rétablir le fond blanc
        self.entree.configure(bg ='white')
        #Enlève les caractères présents
        self.entree.delete(0, len(self.v1ch)) 

## Programme principal

f = Application()        # instanciation de l'objet application