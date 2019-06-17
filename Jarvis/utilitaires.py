#Fichier python pour ranger les fonctions utilitaires

#Importations
import tkinter as tki

#Definition de la classe ListeFonctions
class ListeFonctions():

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Fonction dédiée à l'affichage de la console en tkinter
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
        self.txt = tki.Text(self.frameTexte, borderwidth=3, relief="sunken", bg=self.fondCouleur, foreground=self.texteCouleur, insertbackground=self.insertbg)
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        #Initialisation du curseur
        self.txt.focus_set()

        # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(self.frameTexte, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Fonction pour régler les tags et les bind (programmation évènementielle)
    def fonction_evenementsTags(self):
        #Evenements
        self.root.bind('<KeyPress-Return>',self.fonction_recuptexteconsole)
        self.root.bind('<Control-e>',self.commande_nettoyer)
        #Gestion des tags
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)
        self.txt.tag_configure('input',foreground=self.couleurInput)

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Fonction qui récupère la commande écrite par l'utilisateur
    def fonction_recuptexteconsole(self,event):
        if self.mode == 'console':
            #Récupération de la commande
            self.commande = self.txt.get(str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
            self.commande = self.commande.replace('$ ','')

            print('indice = ',self.indexLigne, 'et commande = ',self.commande)
            self.txt.tag_add('admin',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
            self.indexLigne += 1
            self.fonction_commandes()

        if self.mode == 'saisie':
            #Récupération de la commande
            self.saisie = self.txt.get(str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
            self.saisie = self.saisie.replace('>>> ','')
            self.mode = 'console'
            self.txt['foreground'] = 'orangered'  
            self.txt.tag_add('reponse',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
            self.indexLigne += 1
            self.input.set(self.saisie)

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Fonction pour retourner au mode commande
    def fonction_retourCommande(self):
        #Retour à l'invite de commande
        self.txt.insert(tki.INSERT,  "$ ")
        self.txt.tag_add('admin',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Fonction pour afficher une chaine de caractères dans la console
    def fonction_ecrireLigne(self,chaine):
        chaine = chaine + "\n"
        self.txt.insert(tki.INSERT, chaine)
        self.txt.tag_add('reponse',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        self.indexLigne += 1
        self.txt.yview('scroll',1,'pages')

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Fonction input
    def fonction_input(self,chaine):
        #Affichage
        chaine = chaine + "\n"
        self.txt.insert(tki.INSERT, chaine)
        self.txt.tag_add('input',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        self.indexLigne += 1


        self.txt.insert(tki.INSERT,  ">>> ")
        self.txt.yview('scroll',1,'pages')
        self.txt.tag_add('input',str(self.indexLigne)+'.0 linestart',str(self.indexLigne)+'.0 lineend')
        if self.etatLumiere == 'jour':
            self.txt['foreground'] = 'black'
        if self.etatLumiere == 'nuit':
            self.txt['foreground'] = 'white'  

        #Changement de mode
        self.mode = 'saisie'

        #Attente de la valeur
        self.root.wait_variable(self.input)

        return self.input.get()


#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o


    #Fonction pour afficher automatiquement un tableau
    def fonction_affichageTableau(self,tableau, nbreCaracteres):
        for i in range(len(tableau)):
            chaine = ''
            for j in range(len(tableau[i])):
                while len(tableau[i][j]) <= nbreCaracteres[j]:
                    tableau[i][j] = tableau[i][j] + ' '
                chaine = chaine + tableau[i][j]
            self.fonction_ecrireLigne(chaine)



