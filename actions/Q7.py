import tkinter as tk
from utils import display
from tkinter import ttk
from utils import db

labels=[]
class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(1900, 600, self)
        self.title('Q7 : gérer les travaux de rénovation')
        self.bind('<Escape>', lambda e: self.destroy())
        display.defineGridDisplay(self, 15, 15)
        ###ttk.Label(self, text="""Proposer des fonctionnalités permettant de gérer l'ajout, modification et suppression pour un type de travaux""",
        ###          wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)
        ttk.Label(self, text='Selectionnez une action : ', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=0, column=3)
        self.input = ttk.Combobox(self, values=["Ajout","Modifier","Suprimer"], state="readonly")
        self.input.current(0)
        #self.input.bind('<<ComboboxSelected>>', self.select)
        self.input.grid(row=0, column=4)

        ttk.Label(self, text='Veuillez indiquer le type de travaux :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=1, column=3)    
        choix=["Photovoltaïque","Chauffage","Isolation"] 
        self.input2 = ttk.Combobox(self, values=choix, state="readonly")
        self.input2.current(0)
        self.input2.grid(row=1, column=4)
        self.input2.bind('<<ComboboxSelected>>', self.select)

    def select(self, event):
        print(self.input.get())
        if self.input.get() == "Ajout":
            self.ajout(self.input2)
        elif self.input.get() == "Modifier":
            self.modifier
        elif self.input.get() == "Suprimer":
            self.suprimer
            
    # def ajoutMain(self):
        
    #     ttk.Label(self, text='Veuillez indiquer le type de travaux :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=1, column=3)    
    #     choix=["Photovoltaïque","Chauffage","Isolation"] 
    #     self.input = ttk.Combobox(self, values=choix, state="readonly")
    #     self.input.current(0)
    #     self.input.bind('<<ComboboxSelected>>', self.ajout)
    #     
    
        
        
    def ajout(self, event):
        bout=None
        for i in labels:
            print(i)
            if i:
                i.destroy()
        if bout:
            bout.destroy()
        labels.clear()
        print(event.get())                  
        ttk.Label(self, text='Veuillez indiquer les valeurs à ajouter :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=2, column=3, columnspan=8)
        ttk.Label(self, text='id_travaux:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=0)
        self.id_travaux_entry = ttk.Label(self,text="auto")
        self.id_travaux_entry.grid(row=4, column=0)
        labels.append(self.id_travaux_entry)

        ttk.Label(self, text='cout_total_ht:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=1)
        self.cout_total_ht_entry = ttk.Entry(self)
        self.cout_total_ht_entry.grid(row=4, column=1)
        labels.append(self.cout_total_ht_entry)


        ttk.Label(self, text='cout_induit_ht:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=2)
        self.cout_induit_ht_entry = ttk.Entry(self)
        self.cout_induit_ht_entry.grid(row=4, column=2)
        labels.append(self.cout_induit_ht_entry)

        ttk.Label(self, text='annee_travaux:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=3)
        self.annee_travaux_entry = ttk.Entry(self)
        self.annee_travaux_entry.grid(row=4, column=3)
        labels.append(self.annee_travaux_entry)

        ttk.Label(self, text='code_departement:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=4)
        self.code_departement_entry = ttk.Entry(self)
        self.code_departement_entry.grid(row=4, column=4)
        labels.append(self.code_departement_entry)

        ttk.Label(self, text='code_region:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=5)
        self.code_region_entry = ttk.Entry(self)
        self.code_region_entry.grid(row=4, column=5)
        labels.append(self.code_region_entry)

        ttk.Label(self, text='type_logement:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=8)
        self.type_logement_entry = ttk.Entry(self)
        self.type_logement_entry.grid(row=4, column=8)
        labels.append(self.type_logement_entry)

        ttk.Label(self, text='anne_construction_logement:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=9)
        self.anne_construction_logement_entry = ttk.Entry(self)
        self.anne_construction_logement_entry.grid(row=4, column=9)
        labels.append(self.anne_construction_logement_entry)
    
        if(event.get()=="Photovoltaïque"):
            #('puissance_installee','type_panneaux')
            labels.append(ttk.Label(self, text='puissance_installee:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=0))
            self.puissance_installee_entry = ttk.Entry(self)
            self.puissance_installee_entry.grid(row=6, column=0)
            labels.append(self.puissance_installee_entry)

            labels.append(ttk.Label(self, text='type_panneaux:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=1))
            self.type_panneaux_entry = ttk.Combobox(self, values=["Polycristallin","Monocristallin"], state="readonly")
            self.type_panneaux_entry.grid(row=6, column=1, columnspan=2)
            labels.append(self.type_panneaux_entry)
            
            bout = ttk.Button(self, text='Ajouter', command=self.ajoutPhotovoltaique).grid(row=7, column=0)
            #labels.append(bout)
    
        elif(event.get()=="Chauffage"):
            #('énergie_avant_travaux','energie_installee','generateur','type_chaudiere')
            labels.append(ttk.Label(self, text='énergie_avant_travaux:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=0))
            self.energie_avant_travaux_entry = ttk.Entry(self)
            self.energie_avant_travaux_entry.grid(row=6, column=0)
            labels.append(self.energie_avant_travaux_entry)
            
            labels.append(ttk.Label(self, text='energie_installee:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=1))
            self.energie_installee_entry = ttk.Entry(self)
            self.energie_installee_entry.grid(row=6, column=1)
            labels.append(self.energie_installee_entry)
            
            labels.append(ttk.Label(self, text='generateur:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=2))
            self.generateur_entry = ttk.Entry(self)
            self.generateur_entry.grid(row=6, column=2)
            labels.append(self.generateur_entry)
            
            labels.append(ttk.Label(self, text='type_chaudiere:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=3))
            self.type_chaudiere_entry = ttk.Entry(self)
            self.type_chaudiere_entry.grid(row=6, column=3)
            labels.append(self.type_chaudiere_entry)
            
            bout=ttk.Button(self, text='Ajouter', command=self.ajoutChauffage).grid(row=7, column=0)
            #labels.append(bout)
        
        elif(event.get()=="Isolation"):
            #('poste','type_isolant','epaisseur_isolant','surface')
            labels.append(ttk.Label(self, text='poste_isolation:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=0))
            self.poste_entry = ttk.Entry(self)
            self.poste_entry.grid(row=6, column=0)
            labels.append(self.poste_entry)
            
            labels.append(ttk.Label(self, text='type_isolant:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=1))
            self.type_isolant_entry = ttk.Entry(self)
            self.type_isolant_entry.grid(row=6, column=1)
            labels.append(self.type_isolant_entry)
            
            labels.append(ttk.Label(self, text='epaisseur:', anchor="center", font=('Helvetica', '10')).grid(row=5, column=0))
            self.epaisseur_isolant_entry = ttk.Entry(self)
            self.epaisseur_isolant_entry.grid(row=6, column=0)
            labels.append(self.epaisseur_isolant_entry)
            
            bout=ttk.Button(self, text='Ajouter', command=self.ajoutIsolation).grid(row=7, column=0)
            #labels.append(bout)
         # On place un label sans texte, il servira à afficher les erreurs
        self.errorLabel = ttk.Label(self, anchor="center", font=('Helvetica', '10', 'bold'))
        self.errorLabel.grid(columnspan=3, row=12, sticky="we")
        
    
    def modifier(self,event):
        for i in labels:
            i.grid_remove()
    
    def suprimer(self,event):
        for i in labels:
            i.grid_remove()
        if(event.widget.get()=="Photovoltaïque"):
            ttk.Label(self, text='Veuillez indiquer les valeurs à suprimer :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=2, column=3, columnspan=8)
            ttk.Label(self, text='id_travaux:', anchor="center", font=('Helvetica', '10')).grid(row=3, column=0)
            self.id_travaux_entry = ttk.Entry(self)
            self.id_travaux_entry.grid(row=4, column=0)
            ttk.Button(self, text='Suprimer', command=self.suprimerPhotovoltaique).grid(row=7, column=0)
    
    def getMaxId(self):
        cursor = db.data.cursor()
        id_travaux_phot = cursor.execute("""SELECT MAX(id_travaux) FROM TravauxPhotovoltaique""").fetchone()[0] + 1
        id_travaux_chauff = cursor.execute("""SELECT MAX(id_travaux) FROM TravauxChauffage""").fetchone()[0] + 1
        id_travaux_isol = cursor.execute("""SELECT MAX(id_travaux) FROM TravauxIsolation""").fetchone()[0] + 1
        return max(id_travaux_phot,id_travaux_chauff,id_travaux_isol)
        
    def ajoutPhotovoltaique(self):
        query="""INSERT INTO TravauxPhotovoltaique (id_travaux,cout_total_ht,cout_induit_ht,annee_travaux,
                                    code_departement,code_region,type_logement,anne_construction_logement,
                                    puissance_installee,type_panneaux) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        id_travaux = self.getMaxId()
        try:
            
            cursor = db.data.cursor()
            result = cursor.execute(query, (id_travaux, self.cout_total_ht.get(), self.cout_induit_ht.get(),
                                            self.annee_travaux.get(), self.code_departement.get(), self.code_region.get(),
                                            self.type_logement.get(), self.anne_construction_logement.get(),
                                            self.puissance_installee.get(), self.type_panneaux.get()))

            # S'il y a une erreur, on l'affiche à l'utilisateur
        except Exception as e:
            self.errorLabel.config(foreground='red', text="Erreur : " + repr(e))
        else:
            self.errorLabel.config(foreground='green', text="Ajout réussi !")
            
    def ajoutChauffage(self):
        query="""INSERT INTO TrvauxChauffage (id_travaux,cout_total_ht,cout_induit_ht,annee_travaux,
                                    code_departement,code_region,type_logement,anne_construction_logement,
                                    energie_avant_travaux,energie_installee,generateur,type_chaudiere)
                                    VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        id_travaux = self.getMaxId()
        try:
            cursor = db.data.cursor()
            result = cursor.execute(query, (id_travaux, self.cout_total_ht.get(), self.cout_induit_ht.get(),
                                            self.annee_travaux.get(), self.code_departement.get(), self.code_region.get(),
                                            self.type_logement.get(), self.anne_construction_logement.get(),
                                            self.energie_avant_travaux.get(), self.energie_installee.get(),
                                            self.generateur.get(), self.type_chaudiere.get()))

        # S'il y a une erreur, on l'affiche à l'utilisateur
        except Exception as e:
            self.errorLabel.config(foreground='red', text="Erreur : " + repr(e))
        else:
            self.errorLabel.config(foreground='green', text="Ajout réussi !")
            
    def ajoutIsolation(self):
        query="""INSERT INTO TravauxIsolation (id_travaux,cout_total_ht,cout_induit_ht,annee_travaux,
                                    code_departement,code_region,type_logement,anne_construction_logement,
                                    poste_isolation,type_isolant,epaisseur_isolant,surface)
                                    VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        id_travaux = self.getMaxId()
        try:
            cursor = db.data.cursor()
            result = cursor.execute(query, (id_travaux, self.cout_total_ht.get(), self.cout_induit_ht.get(),
                                            self.annee_travaux.get(), self.code_departement.get(), self.code_region.get(),
                                            self.type_logement.get(), self.anne_construction_logement.get(),
                                            self.poste.get(), self.type_isolant.get(),
                                            self.epaisseur_isolant.get(), self.surface.get()))
        
        # S'il y a une erreur, on l'affiche à l'utilisateur
        except Exception as e:
            self.errorLabel.config(foreground='red', text="Erreur : " + repr(e))
        else:
            self.errorLabel.config(foreground='green', text="Ajout réussi !")
            
