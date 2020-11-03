#!/usr/bin/python3

from tkinter import 
from tkinter.filedialog import *
from tkinter import messagebox

import os
import re


class renommage:
    root = Tk()

    def __init__(self):
        self.root.title('Renommage')
        self.winSize()
        self.btn_dossier = Button(self.root, text='Selectionner le dossier de Renommage', command=self.loaddirectory)
        self.btn_dossier.pack()

        self.labelFrame1 = LabelFrame(self.root, text='liste de(s) fichier(s)', bg='white')
        self.labelFrame1.pack()

        self.labelFrame2 = LabelFrame(self.root, text='Modification')
        self.labelFrame2.pack()

        self.labelModification = Label(self.labelFrame2, text='')
        self.labelModification.pack()
        #	self.labelModification.pack_forget()

        labelDebutIncrement = Label(self.labelFrame2, text='Debut incrementation')
        labelDebutIncrement.pack()
        self.Increment = IntVar();
        self.saisie = Entry(self.labelFrame2, textvariable=self.Increment)
        self.saisie.pack()

        LabelAjoutTexte = Label(self.labelFrame2, text='Ajouter texte?')
        LabelAjoutTexte.pack()

        self.variable1 = StringVar()
        self.variable1.set('non')
        radio1 = Radiobutton(self.labelFrame2, variable=self.variable1, text='oui', value='oui',
                             command=self.enableAjoutTexte)
        radio2 = Radiobutton(self.labelFrame2, variable=self.variable1, text='non', value='non',
                             command=self.enableAjoutTexte)
        radio1.pack()
        radio2.pack()

        self.TexteAjouter = StringVar();
        self.saisie2 = Entry(self.labelFrame2, textvariable=self.TexteAjouter, state='disabled')
        self.saisie2.pack()

        LabelGarderTexte = Label(self.labelFrame2, text='Garder Texte original?')
        LabelGarderTexte.pack()
        self.variable2 = StringVar()
        self.variable2.set('non')
        radio1 = Radiobutton(self.labelFrame2, variable=self.variable2, text='oui', value='oui',
                             command=self.enableGarderTexte)
        radio2 = Radiobutton(self.labelFrame2, variable=self.variable2, text='non', value='non',
                             command=self.enableGarderTexte)
        radio1.pack()
        radio2.pack()

        LabelTexteOg = Label(self.labelFrame2, text='a partir de combien de caractères conserver le texte original?')
        LabelTexteOg.pack()
        self.nbCharac = IntVar();
        self.saisie3 = Entry(self.labelFrame2, textvariable=self.nbCharac, state='disabled')
        self.saisie3.pack()

        self.btn_valider = Button(self.labelFrame2, text='Valider')
        self.btn_valider.pack()

    def affiche(self):
        self.root.mainloop()

    def enableAjoutTexte(self):
        if self.variable1.get() == 'oui':
            self.saisie2.config(state='normal')
        else:
            self.saisie2.config(state='disabled')

    def enableGarderTexte(self):
        if self.variable2.get() == 'oui':
            self.saisie3.config(state='normal')
        else:
            self.saisie3.config(state='disabled')

    def winSize(self):
        screen_x = self.root.winfo_screenwidth()
        screen_y = self.root.winfo_screenheight()
        window_x = 800
        window_y = 600

        posX = (screen_x // 2) - (window_x // 2)
        posY = (screen_y // 2) - (window_y // 2)

        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        self.root.geometry(geo)

    def debutIncrementation(self):
        saisie = Entry(self.root, textvariable=saisie)
        saisie.pack()
        return saisie.get()

    def loaddirectory(self):
        directory = askdirectory()

        # cache le button select dossier
        self.btn_dossier.pack_forget()
        self.renommer(directory)

    def ajoutTexte(self):
        result = messagebox.askquestion("Ajout Texte", "Souhaitez vous ajouter du texte?")
        if result == 'yes':
            return True
        else:
            return False

    def garderTexteOriginal(self):
        rep = askquestion("Garder Texte", "Souhaitez vous garder le texte Original?")
        if result == 'yes':
            return True
        else:
            return False

    def init(self):
        self.saisie.config(state='disabled')
        self.variable1.set('non')
        self.variable2.set('non')
        self.saisie2.insert(0, '')
        self.saisie3.insert(0, '')

    def renommer(self, directory):

        dossierInitiale = os.getcwd()
        os.chdir(directory)

        for rep, souRep, files in os.walk('.'):
            self.photos = files
            for fileName in files:
                lbl = Label(self.labelFrame1, text=fileName)
                lbl.pack()
            break

        print(self.photos)

        for i in self.photos:
            self.labelModification.config(text='modif de :' + i)
            self.fileName = i
            self.btn_valider.config(command=lambda: self.Valider())
            self.init()

    def Valider(self):
        regExtension = "\.\w+$"
        match = re.search(regExtension, self.fileName)
        extension = match.group()
        positions = match.span()
        debut, fin = positions
        fileNameWExt = self.fileName[:debut]

        Increment = self.Increment.get()
        print(Increment)

        newName = "%03d" % Increment

        if self.variable1.get() == 'oui':
            texte = self.TexteAjouter.get()
            print("ajouter : " + texte)
            newName = newName + ' - ' + texte

        if self.variable2.get() == 'oui':
            debutConservation = self.nbCharac.get()
            print("garder : " + str(debutConservation))
            newName = newName + ' - ' + fileNameWExt[debutConservation:]

        newName += extension

        if messagebox.askquestion("Valider la modificaition", "Valider le nouveau blaze ? : " + newName) == 'yes':
            os.rename(self.fileName, newName)
        Increment += 1


test = renommage()
test.affiche()
