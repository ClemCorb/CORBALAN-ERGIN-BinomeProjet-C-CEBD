import tkinter as tk
from utils import display
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q7 : gérer les travaux de rénovation')
        self.bind('<Escape>', lambda e: self.destroy())
        display.defineGridDisplay(self, 6, 6)
        ###ttk.Label(self, text="""Proposer des fonctionnalités permettant de gérer l'ajout, modification et suppression pour un type de travaux""",
        ###          wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)
        ttk.Label(self, text='Selectionnez une action : ', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=0, column=3)
        self.input = ttk.Combobox(self, values=["Ajout","Modifier","Suprimer"], state="readonly")
        self.input.current(0)
        self.input.bind('<<ComboboxSelected>>', self.select)
        self.input.bind('<Return>', self.select)
        self.input.grid(row=0, column=4)
        
    def select(self, event):
         if self.input.get() == "Ajout":
             self.ajoutMain()
        # elif self.input.get() == "Chauffage":
        #     self.destroy()
        #     self.window = Chauffage(self)
        # elif self.input.get() == "Isolation":
        #     self.destroy()
        #     self.window = Isolation(self)
            
    def ajoutMain(self):
        ttk.Label(self, text='Veuillez indiquer le type de travaux :', anchor="center", font=('Helvetica', '10', 'bold')).grid(row=1, column=3)    
        choix=["Photovoltaïque","Chauffage","Isolation"] 
        self.input = ttk.Combobox(self, values=choix, state="readonly")
        self.input.current(0)
        self.input.bind('<<ComboboxSelected>>', self.ajout)
        self.input.grid(row=1, column=4)
        
    def ajout(self, event):
        #if self.input.get() == "Photovoltaïque":
        #     self.destroy()
        #     self.window = Photovoltaique(self)
        # elif self.input.get() == "Chauffage":
        #     self.destroy()
        #     self.window = Chauffage(self)
        # elif self.input.get() == "Isolation":
        #     self.destroy()
        #     self.window = Isolation(self)
        print("ok")
