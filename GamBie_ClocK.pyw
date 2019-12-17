#import :
import tkinter as tk
import requests as rq #faire pip install requests
import tkinter.font as tkFont
import tkinter.messagebox as tkmsg

class Application (tk.Tk):
    '''Classe de la fenetre principale'''
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 50
        self.Creation_frame()
        self.Creation_menu()
        self.Creer_widgets()
        self.title('GamBie ClocK')

    def Creation_frame(self):
        '''Methode pour la création des Frames'''
        self.frmHeader = tk.Frame(self)
        self.frmBody = tk.Frame(self)
        self.frmFooter = tk.Frame(self)
        self.frmHeader.pack()
        self.frmBody.pack()
        self.frmFooter.pack() 

    def Creer_widgets(self):
        '''Methode pour creer les widgets'''
        self.varMessage = tk.StringVar()
        self.varMessage.set("message")
        #Création des boutons, entry et text box
        self.champsMessage = tk.Entry(self.frmBody, textvariable = self.varMessage, justify = 'center')
        self.bouttonEnvois = tk.Button(self.frmBody, text = "Envois", command = self.Envois_message, width = 10)
        self.btnTemperature = tk.Button(self.frmBody,text = 'Afficher', command = lambda : self.Envois_parametre('temperature'), width = 10)
        self.lblTemperature = tk.Label(self.frmBody, text = 'Température / Humidité ?')
        self.txtRetour = tk.Text(self.frmBody, width = self.size)
        #Collage des widgets
        self.champsMessage.grid(column = 0, row = 0, sticky = 'e')
        self.bouttonEnvois.grid(column = 1, row = 0, sticky = 'w')
        self.lblTemperature.grid(column = 0, row = 1, sticky = 'e')
        self.btnTemperature.grid(column = 1,row = 1, sticky = 'w')
        self.txtRetour.grid(column = 0, row = 2, columnspan = 2)

    def Envois_message(self):
        '''Méthode pour l'envois du message au serveur'''
        stgMessage =  'http://' + Lecture_ecriture_config("", 'lecture') + '/message:' + self.varMessage.get() + '*'
        stgMessage = stgMessage.replace(" ","_")
        print ('Chaine envoye : ' + stgMessage) 
        r = rq.get(stgMessage)
        retour = 'Envois du message \"' + self.varMessage.get() + '\"\n'
        retour += 'Reception : ' + r.text + '\n'
        if r.text.find('recu'):
            retour += '\n***********************OK*************************\n\n'
        self.txtRetour.insert(tk.END, retour)


    def Creation_menu(self):
        '''Methode pour la création du menu'''
        self.menuPrincipal = tk.Menu()
        self.menuPrincipal.add_command(label = 'Paramètre', command = self.Parametre)
        self.menuPrincipal.add_command(label = 'Quitter', command = self.quit)
        self.config(menu  = self.menuPrincipal)

    def Parametre(self):
        '''Méthode pour la gestion des parametres'''
        #Création d'une nouvelle fenetre
        self.fenetreParametre = tk.Toplevel()
        self.fenetreParametre.title('Parametre')
        self.fenetreParametre.focus_set()

        #Frame de placement
        self.frmIp = tk.LabelFrame(self.fenetreParametre, relief = 'groove', text = 'Réglage IP', padx = 5, pady = 5)
        self.frmBouton = tk.LabelFrame(self.fenetreParametre,relief = 'groove', text = 'Bouton config', padx = 5, pady = 5)
        self.frmTemps = tk.LabelFrame(self.fenetreParametre, relief = 'groove', text = 'Réglage temps', padx = 5, pady = 5)
        self.frmIp.grid(column = 0, row = 0, columnspan = 2)
        self.frmBouton.grid(column = 0, row = 1)
        self.frmTemps.grid(column = 1, row = 1)

        #Variable de contrôle
        self.varIp = tk.StringVar()
        self.varIp.set(Lecture_ecriture_config("", mode="lecture"))
        self.varTempo = tk.StringVar()
        self.varTempo.set("30")
        self.varActualisation = tk.StringVar()
        self.varActualisation.set("5")

        #Création des widgets
        self.lblIp = tk.Label(self.frmIp, text = 'ip : ')
        self.entIp = tk.Entry(self.frmIp,textvariable = self.varIp)
        self.btnIp = tk.Button(self.frmIp,text = 'Appliquer', command = lambda : Lecture_ecriture_config(self.varIp.get(), self.fenetreParametre, 'ecriture'))
        self.btnEte = tk.Button(self.frmBouton,text = 'Ete/Hiver', command = lambda :  self.Envois_parametre ("ete"), width = 10)
        self.btnMaintient = tk.Button(self.frmBouton, text = 'Maintient', command = lambda : self.Envois_parametre("maintient"), width = 10)
        self.btnTempo = tk.Button(self.frmTemps, text = 'Appliquer', command = lambda : self.Envois_parametre("tempo"), width = 10)
        self.btnActualisation = tk.Button(self.frmTemps, text = 'Appliquer', command = lambda : self.Envois_parametre("actualisation"), width = 10)
        self.entTempo = tk.Entry(self.frmTemps,textvariable = self.varTempo, width = '5', justify = 'right')
        self.entActualisation = tk.Entry(self.frmTemps, textvariable = self.varActualisation, width = '5', justify = 'right')
        self.lblTempo = tk.Label(self.frmTemps,text = 's')
        self.lblActualisation = tk.Label(self.frmTemps,text = 'min')
        


        #Collage des widgets
        self.lblIp.grid(column = 0, row =0, sticky = 'e')
        self.entIp.grid(column = 1, row = 0, sticky = 'w', pady = 10, padx = 10)
        self.btnIp.grid(column = 2, row = 0, sticky = 'w')

        self.btnEte.grid(column = 0, row = 0, sticky = 'w', pady = 10, padx = 10)
        self.btnMaintient.grid(column = 0, row = 1, sticky = 'w', pady = 10, padx = 10)

        self.entTempo.grid(column = 0, row = 0)
        self.entActualisation.grid(column = 0, row = 1)
        self.lblTempo.grid(column= 1, row = 0)
        self.lblActualisation.grid(column = 1, row = 1)
        self.btnTempo.grid(column = 2, row = 0, sticky = 'w', pady = 10, padx = 10)
        self.btnActualisation.grid(column = 2,row = 1)



    def Envois_parametre(self,config):
        ip = Lecture_ecriture_config("","lecture")
        debut = 'http://' + ip + '/param:'
        erreur = False

        if config == 'ete':
            r = rq.get(debut + 'ete*')
            print (r.text)

        if config =='maintient':
            r = rq.get(debut + 'maintient*')
            #print (r.text)

        if config =='temperature':
            r = rq.get(debut + 'temperature*')

        if config =='tempo':
            tempo = self.varTempo.get()
            try :
                tempo = int(tempo)
                tempo = tempo *1000
                r = rq.get(debut + 'tempo-' + str(tempo) + "*")
            except ValueError:
                print ("Erreur de valeur, veuillez entrer un nombre")
                tkmsg.showerror('Erreur tempo', "erreur !!\nVeuillez rentrer un nombre !")
                erreur = True
                self.fenetreParametre.focus_set()  

        if config == 'actualisation':
            actualisation = self.varActualisation.get()
            try:
                actualisation = int(actualisation)
                r = rq.get(debut + "actualisation-" + str(actualisation) +"*")
            except ValueError:
                print ("Erreur de valeur, veuillez entrer un nombre ")
                tkmsg.showerror('Erreur actualisation',"erreur !!\nVeuillez rentrer un nombre !" )
                erreur = True
                self.fenetreParametre.focus_set()
        if not(erreur): 
            retour = 'Reception : ' + r.text + '\n'
            if r.text.find('recu'):
                retour += '\n***********************OK*************************\n\n'         
                self.txtRetour.insert(tk.END, retour)
            else:
                self.txtRetour.insert(tk.END,'-----Echec----\n')

def Lecture_ecriture_config(text, fenetre = '', mode = 'lecture'):
    if mode == 'lecture':
        with open("config.txt", "r") as fichier:
            return fichier.read()
    if mode == 'ecriture':
        with open("config.txt", "w") as fichier:
            print ('ecriture de : ',text)
            fichier.write(text)
            tkmsg.showinfo('Info', 'Ip enregristrée')
            fenetre.focus_set()
            


if __name__ == "__main__" :
    app = Application()    
    app.mainloop()