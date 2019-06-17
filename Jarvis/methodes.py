#Fichier python qui contient une liste de méthodes utilitaires

#Importations
import tkinter as tki

class ListeMethodes():

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui transforme un nombre décimal en nombre binaire
    def commande_bin(self):
        #Calcul du nombre binaire
        decimal = int(self.fonction_input('Saisir le nombre décimal'))
        reste = 0
        binaire,S = [],[]
        while decimal>0:
            reste=decimal%2
            decimal=decimal//2
            binaire.append(reste)

        Long=len(binaire)
        for i in range(0,Long):
            S.append(str(binaire[Long-1-i]))

        #Affichage du nombre en binaire
        self.fonction_ecrireLigne(''.join(S))

        #Retour en mode commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui transforme un nombre décimal en nombre hexadécimal
    def commande_hex(self):
        #Calcul
        decimal = int(self.fonction_input('Saisir le nombre décimal'))
        hexa = hex(decimal)
        #Affichage du nombre en hexadecimal
        self.fonction_ecrireLigne(str(hexa))

        #Retour en mode commande
        self.fonction_retourCommande()


#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui efface les écritures dans la console
    def commande_nettoyer(self,event):
        #Nettoyage
        self.indexLigne = 1
        self.txt.delete('1.0', tki.END)

        #Retour à l'invite de commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Commande qui donne la date
    def commande_date(self):
        #Importations
        from datetime import datetime
        #Affichage de la date locale
        date = datetime.now()
        self.fonction_ecrireLigne("Aujourd'hui on est le {}/{}/{}.".format(str(date.day),str(date.month),str(date.year)))

        #Retour à l'invite de commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Commande qui donne l'heure
    def commande_heure(self):
        #Importations
        from datetime import datetime
        #Affichage de l'heure locale
        date = datetime.now()
        self.fonction_ecrireLigne("Il est {}:{}.".format(str(date.hour),str(date.minute)))

        #Retour à l'invite de commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Commande qui met la console en mode jour (fond blanc)
    def commande_jour(self):
        self.etatLumiere = 'jour'
        #Mettre la console en mode jour
        self.entreeCouleur = 'orangered'
        self.texteCouleur = 'orangered'
        self.reponseCouleur = 'black'
        self.fondCouleur = 'white'
        self.txt['insertbackground'] = 'black'

        #Mise à jour
        self.txt['foreground'] = self.texteCouleur
        self.txt['background'] = self.fondCouleur
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)

        #Message
        self.fonction_ecrireLigne("La console est maintenant en mode jour.")

        #Retour à l'invite de commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui met la console en mode nuit (fond noir)
    def commande_nuit(self):
        self.etatLumiere = 'nuit'
        #Mettre la console en mode jour
        self.entreeCouleur = 'orangered'
        self.texteCouleur = 'orangered'
        self.reponseCouleur = 'white'
        self.fondCouleur = 'black'
        self.txt['insertbackground'] = 'white'

        #Mise à jour
        self.txt['foreground'] = self.texteCouleur
        self.txt['background'] = self.fondCouleur
        self.txt.tag_configure('admin',foreground=self.entreeCouleur)
        self.txt.tag_configure('reponse',foreground=self.reponseCouleur)

        #Message
        self.fonction_ecrireLigne("La console est maintenant en mode nuit.")

        #Retour à l'invite de commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui exécute un programme dans le répertoire courant
    def commande_exec(self):
        #Importations
        from subprocess import call as lancerProgramme
        from subprocess import Popen
        import os

        #Lancer le fichier
        if self.commande[1] == 'word': os.system("cmd \"C:/Users/cleme/Desktop/console/raccourcis/word.lnk\"")
        elif self.commande[1] == 'excel': Popen(["raccourcis/word.lnk"]);
        elif self.commande[1] == 'powerpoint': Popen(["C:/Program Files/WindowsApps/Microsoft.Office.Desktop.PowerPoint_16051.11425.20204.0_x86__8wekyb3d8bbwe/Office16/POWERPNT.exe"]);
        else:
            lancerProgramme("python C:/Users/cleme/Desktop/console/raccourcis/"+self.commande[1]+".py")

        #Message
        self.fonction_ecrireLigne('Le programme '+str(self.commande[1])+' va être lancé.')

        #Retour à la commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande pour exécuter un calcul simple
    def commande_calcul(self):
        self.fonction_ecrireLigne(str(eval(self.fonction_input('Saisir le calcul'))))
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Renvoie le bulletin meteo du jour
    def commande_meteo(self):
        import requests
        from bs4 import BeautifulSoup

        #Telechargement de la page meteo France
        req = requests.get('http://www.my-meteo.com/meteo-'+self.commande[1]+'/'+self.commande[2]+'/#aujourdhui');
        req1 = requests.get('http://www.my-meteo.com/meteo-france/compiegne/12-jours.html');
        #Parsing du code avec bs4
        soup = BeautifulSoup(req.text, "lxml")
        #Initialisation résultats
        listePrevisions = []

        #Recherche des éléments intéressants et mise en forme
        previsions        = soup.find_all(class_="previsions_journee")
        matin_temperature = previsions[0].find(class_='temperature').get_text()
        matin_temperature = matin_temperature.split('Ressenti')
        matin_temperature = matin_temperature[0]
        matin_description = previsions[0].find(class_='temps').get_text()
        matin_vent        = previsions[0].find(class_='vent').get_text()
        matin_pluie       = previsions[0].find(class_='pluie').get_text()
        matin_humidite    = previsions[0].find(class_='humidite').get_text()
        matin_pression    = previsions[0].find(class_='pression').get_text()
        aprem_temperature = previsions[1].find(class_='temperature').get_text()
        aprem_temperature = aprem_temperature.split('Ressenti')
        aprem_temperature = aprem_temperature[0]
        aprem_description = previsions[1].find(class_='temps').get_text()
        aprem_vent        = previsions[1].find(class_='vent').get_text()
        aprem_pluie       = previsions[1].find(class_='pluie').get_text()
        aprem_humidite    = previsions[1].find(class_='humidite').get_text()
        aprem_pression    = previsions[1].find(class_='pression').get_text()
        soir_temperature  = previsions[2].find(class_='temperature').get_text()
        soir_temperature  = soir_temperature.split('Ressenti')
        soir_temperature  = soir_temperature[0]
        soir_description  = previsions[2].find(class_='temps').get_text()
        soir_vent         = previsions[2].find(class_='vent').get_text()
        soir_pluie        = previsions[2].find(class_='pluie').get_text()
        soir_humidite     = previsions[2].find(class_='humidite').get_text()
        soir_pression     = previsions[2].find(class_='pression').get_text()


        #Affichage dans la console
        self.fonction_ecrireLigne('Voici le bulletin météo du jour :')
        self.fonction_ecrireLigne(' ')
        self.fonction_ecrireLigne('Dans la matinée :')
        self.fonction_ecrireLigne('Température : '+matin_temperature)
        self.fonction_ecrireLigne(matin_description)
        self.fonction_ecrireLigne('Vent : '+matin_vent)
        self.fonction_ecrireLigne(matin_pluie)
        self.fonction_ecrireLigne(matin_humidite)
        self.fonction_ecrireLigne(matin_pression)
        self.fonction_ecrireLigne(' ')
        self.fonction_ecrireLigne("Dans l'après midi :")
        self.fonction_ecrireLigne('Température : '+aprem_temperature)
        self.fonction_ecrireLigne(aprem_description)
        self.fonction_ecrireLigne('Vent : '+aprem_vent)
        self.fonction_ecrireLigne(aprem_pluie)
        self.fonction_ecrireLigne(aprem_humidite)
        self.fonction_ecrireLigne(aprem_pression)
        self.fonction_ecrireLigne(' ')
        self.fonction_ecrireLigne('Dans la soirée :')
        self.fonction_ecrireLigne('Température : '+soir_temperature)
        self.fonction_ecrireLigne(soir_description)
        self.fonction_ecrireLigne('Vent : '+soir_vent)
        self.fonction_ecrireLigne(soir_pluie)
        self.fonction_ecrireLigne(soir_humidite)
        self.fonction_ecrireLigne(soir_pression)


        #Retour en mode commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui change le répertoire courant
    def commande_cd(self):

        if self.commande[1] == '~':
            self.repertoireCourant = 'C:/Users/cleme/Desktop/Python/Projets/Conspy'
        elif self.commande[1][0] == '/':
            if self.commande[1][-1] == '/':
                self.repertoireCourant = self.repertoireCourant + self.commande[1][:-1]
            else:
                self.repertoireCourant = self.repertoireCourant + self.commande[1]
        else:
            self.repertoireCourant = self.commande[1]

        self.fonction_ecrireLigne('Répertoire courant actualisé')
        #Retour en mode commande
        self.fonction_retourCommande()  

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande qui affiche le répertoire courant
    def commande_pwd(self):
        self.fonction_ecrireLigne(self.repertoireCourant)
        #Retour en mode commande
        self.fonction_retourCommande()  

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Commande qui donne le rendement brut et le rendement net d'un achat immobillier
    def commande_investissement_locatif(self):
        #Récupération des données
        prixAchat = int(self.fonction_input("Saisir le prix d'achat du bien"))
        prixTravaux = int(self.fonction_input("Saisir le prix des travaux à réaliser"))
        loyerMensuel = int(self.fonction_input("Saisir le loyer mensuel"))
        Notaire = int(self.fonction_input("Saisir le pourcentage du notaire"))
        joursVacances = int(self.fonction_input("Saisir le nombre de jours de vacances locatives"))
        prixAssurance = int(self.fonction_input("Saisir le prix de l'assurance annuelle"))
        prixEntretien = int(self.fonction_input("Saisir le prix de l'entretien annuel "))
        prixGestion = int(self.fonction_input("Saisir le prix de la gestion"))
        prixCopropriete = int(self.fonction_input("Saisir les charges de copropriété"))
        TaxeFonciere = int(self.fonction_input("Saisir le pourcentage de taxe foncière"))

        #Calculs 
        prixNotaire = (Notaire/100)*prixAchat
        loyerAnnuel = 12 * loyerMensuel
        prixVacancesLocatives = loyerAnnuel * (joursVacances / 365)
        prixTaxeFonciere = (loyerAnnuel/2)*(TaxeFonciere/100)
        rendementBrut = (loyerAnnuel*100)/ (prixAchat+prixTravaux+prixNotaire)
        chargesTotales = prixVacancesLocatives + prixAssurance + prixCopropriete + prixGestion + prixEntretien + prixTaxeFonciere
        rendementNet = ((loyerAnnuel - chargesTotales)*100) / (prixAchat+prixTravaux+prixNotaire)

        #Affichage
        self.fonction_ecrireLigne('Rendement Brut : '+str(round(rendementBrut,4))+ '%')
        self.fonction_ecrireLigne('Rendement Net : '+str(round(rendementNet,4))+ '%')

        #Retour en mode commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
    
    #Commande qui retourne la liste des anagrammes d'un mot
    def commande_anagrammes(self):
        #Importations
        from math import factorial

        #Fonction pour calculer le nombre d'anagrammes
        def Nbr_anagrammes(mot):
            resultat = factorial(len(mot))
            lettres = []
            
            for i in range(0,len(mot)):
                if lettres.count(mot[i]) == 0:
                    lettres.append(mot[i])
                    resultat = resultat / factorial(mot.count(mot[i]))
            mot1 = ''
            for i in mot:
                mot1 = mot1+i

            return mot1, resultat
            
        #Fonction pour l'affichage des anagrammes
        def liste_anagrammes(liste_mots, erreur=False, k=0):
            #Test d'arrêt
            n = len(liste_mots)
            #Si les n lettres sont bloquées , retourner rien 
            if k == n-1:
                return []
            #Initialisation de la liste qui va contenir tous les anagrammes
            arbre = []
            
            #Copie de liste_mots dans L
            L = liste_mots[:]
            
            #Boucle récursive sur les lettres qu'il reste
            for i in range(0, n-k):
                if erreur==False or (L not in arbre):
                    #
                    arbre.append(L[:]) 
                    arbre.extend(liste_anagrammes(L, erreur, k+1)[1:])
                #Prend la lettre d'indice k et la remet à la fin de la liste
                L.append(L.pop(k))
            return arbre
            
        ## Programme principal

        #Saisie du mot 
        mot = list(self.fonction_input("Saisir le mot"))

        #Appel des fonctions
        mot1, nombre = Nbr_anagrammes(mot)
        l = liste_anagrammes(mot)

        #Boucle pour transformer les objets listes en str
        resultat = []
        for i in range(0,len(l)):
            mot = "".join(l[i])
            resultat.append(mot)

        #Fonction python qui enlève les doublons d'une liste
        resultat=set(resultat)
        resultat=str(sorted(resultat))

        #Affichage
        self.fonction_ecrireLigne("Le mot "+str(mot1)+" a "+str(int(nombre))+" anagrammes.")
        self.fonction_ecrireLigne('')
        self.fonction_ecrireLigne(resultat)

        #Retour en mode commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Affiche la valeur de pi
    def commande_pi(self):
        #Importations
        from numpy import pi
        self.fonction_ecrireLigne(str(pi))
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Donne les définitions de n'importe quel mot passé en paramètre
    def commande_definition(self):
        #Importations
        import requests
        from bs4 import BeautifulSoup


        #Telechargement de la page meteo France
        req = requests.get('https://www.le-dictionnaire.com/definition/'+self.commande[1]);

        #Parsing du code avec bs4
        soup = BeautifulSoup(req.text, "lxml")

        #Récupération des définitions
        definitions = soup.find(class_='defbox')
        definitions = definitions.find_all('li')
        texte = []
        for i in range(len(definitions)):
            liste = definitions[i].find_all('a')
            ligne = ''
            for i in liste:
                ligne = ligne + i.get_text() + ' '
            texte.append(ligne)

        #Affichage
        for i in texte:
            self.fonction_ecrireLigne(i)
            self.fonction_ecrireLigne(' ')

        #Retour commande
        self.fonction_retourCommande()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande pour lister les anniversaires
    def commande_anniversaires(self):
        #Importation
        import sqlite3

        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/anniv.sq3" 

        #Connection
        conn =sqlite3.connect(fichierDonnees) 
        #Curseur de sécurité
        cur =conn.cursor()

        #Creation database
        cur.execute("SELECT * FROM anniversaires ORDER BY nom")

        liste = []
        for i in cur:
            liste.append([i[0],i[1],i[2]])
        print(liste)

        #Fermeture des connections
        cur.close()
        conn.close()
        self.fonction_ecrireLigne("")
        self.fonction_ecrireLigne("Table des anniversaires")
        self.fonction_ecrireLigne("")

        #Mise en forme de l'affichage
        for i in liste:
            while len(i[0]) < 15:
                i[0] = i[0] + ' '
            while len(i[1]) < 20:
                i[1] = i[1] + ' '
            while len(i[2]) < 10:
                i[2] = i[2] + ' '
            self.fonction_ecrireLigne(i[0]+' '+i[1]+' '+i[2])

        #Retour au mode commande
        self.fonction_retourCommande()





    def commande_anniv_add(self):
        #Importation
        import sqlite3

        prenom = self.fonction_input('Saisir le prénom')
        nom = self.fonction_input('Saisir le nom')
        datenaissance = self.fonction_input('Saisir la date sous format JJ/MM/AAAA')
        donnee = (prenom,nom,datenaissance)


        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/anniv.sq3"

        #Connection
        conn =sqlite3.connect(fichierDonnees) 
        #Curseur de sécurité
        cur =conn.cursor()

        #Insertion
        cur.execute("INSERT INTO anniversaires(prenom, nom, date_naissance) VALUES(?,?,?)", donnee)

        conn.commit()

        #Fermeture des connections
        cur.close()
        conn.close()
        self.commande_anniversaires()



    def commande_anniv_remove(self):
        #Importation
        import sqlite3

        nom = self.fonction_input('Saisir le nom de la personne à enlever de la liste')
        prenom = self.fonction_input('Saisir le prénom de la personne à enlever de la liste')


        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/anniv.sq3"

        #Connection
        conn =sqlite3.connect(fichierDonnees) 
        #Curseur de sécurité
        cur =conn.cursor()
        #Insertion
        cur.execute("DELETE FROM anniversaires WHERE nom= ? and prenom = ?", (nom, prenom))

        conn.commit()

        #Fermeture des connections
        cur.close()
        conn.close()

        self.commande_anniversaires()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

    #Commande pour lister les tâches à réaliser
    def commande_todo(self):
        #Importation
        import sqlite3

        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/todolist.sq3" 

        #Connection
        conn =sqlite3.connect(fichierDonnees) 
        #Curseur de sécurité
        cur =conn.cursor()

        #Creation database
        cur.execute("SELECT * FROM listetache")
        liste = list(cur)

        #Fermeture des connections
        cur.close()
        conn.close()

        #Affichage
        self.fonction_ecrireLigne("")
        self.fonction_ecrireLigne("Liste des tâches")
        self.fonction_ecrireLigne("")

        for i in liste:
            self.fonction_ecrireLigne('-> '+i[1])

        #Retour au mode commande
        self.fonction_retourCommande()





    def commande_todo_add(self):
        #Importation
        import sqlite3

        tache = self.fonction_input('Saisir la tâche à réaliser')

        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/todolist.sq3"

        #Connection
        conn =sqlite3.connect(fichierDonnees) 

        #Curseur de sécurité
        cur =conn.cursor()

        #Insertion
        cur.execute("INSERT INTO listetache(tache) VALUES(?)", (donnee,))
        conn.commit()

        #Fermeture des connections
        cur.close()
        conn.close()


        self.commande_todo()



    def commande_todo_remove(self):
        #Importation
        import sqlite3

        nom = self.fonction_input('Saisir le numéro de la tache à enlever')

        fichierDonnees ="C:/Users/cleme/Desktop/Python/Projets/Conspy/data/anniv.sq3"

        #Connection
        conn =sqlite3.connect(fichierDonnees) 
        #Curseur de sécurité
        cur =conn.cursor()
        donnee = nom
        #Insertion
        cur.execute("DELETE FROM anniversaires WHERE nom=(?)", (donnee,))

        conn.commit()

        #Fermeture des connections
        cur.close()
        conn.close()

        self.commande_anniversaires()

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o


    #Commande pour afficher un texte console
    def commande_print(self):
        texte = self.fonction_input('Saisir le texte à afficher')
        print(texte)
        self.fonction_ecrireLigne(texte)

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o


    def commande_rr_party(self):
        #Importations
        from bs4 import BeautifulSoup
        from data.fichierhtml import codeSource
        from datetime import datetime
        from copy import deepcopy
        import sqlite3

        date = datetime.now()
        date = "{}/{}/{}".format(str(date.day),str(date.month),str(date.year))
        
        for i in range(len(codeSource)):
            soup = BeautifulSoup(codeSource[i], features="lxml")
            titre = soup.find('title')
            titre = titre.get_text()

            listeMembres = soup.find_all('tr', class_= 'odd')

            listeTriee = []

            for i in listeMembres:
                carac = i.find_all('td')
                membre = []

                membre.append(carac[0].get_text())
                membre.append(carac[2].get_text())
                membre.append(carac[7].get_text())
                membre.append(carac[8].get_text())
                membre.append(carac[9].get_text())
                membre.append(carac[13].get_text())
                membre.append(carac[15].get_text())
                membre.append(carac[16].get_text())
                membre.append(date)

                #Insertion dans la base de donnée
                donnee = (membre[0], membre[1],membre[2],membre[3],membre[4], date)
                conn =sqlite3.connect("C:/Users/cleme/Desktop/Informatique/Projets - Python/Conspy/data/joueurs_rr.db") 
                cur =conn.cursor()
                cur.execute("INSERT INTO joueurs(pseudo, level, force, connaissance, endurance, date_enregistrement) VALUES(?,?,?,?,?,?)", donnee)
                conn.commit()
                cur.close()
                conn.close()

                #Append à la liste des membres
                listeTriee.append(membre)

            listeMembres = soup.find_all('tr', class_= 'even')

            for i in listeMembres:
                carac = i.find_all('td')
                membre = []

                membre.append(carac[0].get_text())
                membre.append(carac[2].get_text())
                membre.append(carac[7].get_text())
                membre.append(carac[8].get_text())
                membre.append(carac[9].get_text())
                membre.append(carac[13].get_text())
                membre.append(carac[15].get_text())
                membre.append(carac[16].get_text())
                membre.append(date)

                #Insertion dans la base de donnée
                donnee = (membre[0], membre[1],membre[2],membre[3],membre[4], date)
                conn =sqlite3.connect("C:/Users/cleme/Desktop/Informatique/Projets - Python/Conspy/data/joueurs_rr.db") 
                cur =conn.cursor()
                cur.execute("INSERT INTO joueurs(pseudo, level, force, connaissance, endurance, date_enregistrement) VALUES(?,?,?,?,?,?)", donnee)
                conn.commit()
                cur.close()
                conn.close()

                #Append à la liste 
                listeTriee.append(membre)

            doublons = """
            DELETE FROM joueurs 
            WHERE rowid NOT IN (
            SELECT MIN(rowid) 
            FROM joueurs
            GROUP BY pseudo, date_enregistrement
        ) 
            """

            conn =sqlite3.connect("C:/Users/cleme/Desktop/Informatique/Projets - Python/Conspy/data/joueurs_rr.db") 
            cur =conn.cursor()
            cur.execute(doublons)
            conn.commit()
            cur.close()
            conn.close()

            self.membres = deepcopy(listeTriee)

            self.fonction_affichageTableau(listeTriee, [40, 5, 10, 10, 10, 10, 30, 30, 10])




#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
