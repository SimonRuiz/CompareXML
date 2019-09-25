import os, subprocess
import threading
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import lxml.etree as et
import time
import re

#Class contenant les script de traitement des fichiers XML
class ScriptsXML:
    #fonction qui compare 2 fichier xml, 1 -> 2, créer 1 fichier text
    def compareXML_withpath_1(self, file1, file2, directory_result, name_result):
        TkinterGUI.set_textlog(self, 'Lancement du script !')
        root.update()
        #Init var
        tree_file1 = et.parse(file1)
        root_file1 = tree_file1.getroot()
        tree_file2 = et.parse(file2)
        root_file2 = tree_file2.getroot()
        file1_name = []
        file2_name = []
        file1_name_check = []
        file2_name_check = []
        name_diff = []
        pathresult1 = directory_result + "\\" + name_result + ".txt"
        #Boucle iteration xml fichier 1
        for objectHierarchy in root_file1.iter('Object'):
                if objectHierarchy.get('Name') not in file1_name_check:
                        name = objectHierarchy.get('Name')
                        file1_name_check.append(name)
                        parentpath = ''
                        for objectHierarchyAncestor in list(objectHierarchy.iterancestors()):
                                if objectHierarchyAncestor.get('Name'):
                                        parentpath = objectHierarchyAncestor.get('Name') + ' / ' + parentpath
                        file1_name.append(parentpath + name)
        TkinterGUI.set_textlog(self, 'Etape 1/3')
        root.update()
        #Boucle iteration xml fichier 2
        for objectHierarchy in root_file2.iter('Object'):
                if objectHierarchy.get('Name') not in file2_name_check:
                        name = objectHierarchy.get('Name')
                        file2_name_check.append(name)
                        parentpath = ''
                        for objectHierarchyAncestor in list(objectHierarchy.iterancestors()):
                                if objectHierarchyAncestor.get('Name'):
                                        parentpath = objectHierarchyAncestor.get('Name') + ' / ' + parentpath
                        file2_name.append(parentpath + name)
        TkinterGUI.set_textlog(self, 'Etape 2/3')
        root.update()
        #Compare les differences et les écrits dans un fichier text 1->2
        logfile = open(pathresult1,"w+")
        for name_file1 in file1_name:
                check = False
                for name_file2 in file2_name:
                        if name_file1 == name_file2:
                                check = True
                if check == False:
                        name_diff.append(name_file1)
                        logfile.write(name_file1 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 3/3')
        TkinterGUI.set_textlog(self, 'Comparaison terminé !')
        root.update()
    #fonction qui compare 2 fichier xml, 1 -> 2, 2->1, créer 2 fichier text
    def compareXML_withpath_2(self, file1, file2, directory_result, name_result1, name_result2):
        TkinterGUI.set_textlog(self, 'Lancement du script !')
        root.update()
        #Init var
        tree_file1 = et.parse(file1)
        root_file1 = tree_file1.getroot()
        tree_file2 = et.parse(file2)
        root_file2 = tree_file2.getroot()
        file1_name = []
        file2_name = []
        file1_name_check = []
        file2_name_check = []
        pathresult1 = directory_result + "\\" + name_result1 + ".txt"
        pathresult2 = directory_result + "\\" + name_result2 + ".txt"
        #Boucle iteration xml fichier 1
        for objectHierarchy in root_file1.iter('Object'):
                if objectHierarchy.get('Name') not in file1_name_check:
                        name = objectHierarchy.get('Name')
                        file1_name_check.append(name)
                        parentpath = ''
                        for objectHierarchyAncestor in list(objectHierarchy.iterancestors()):
                                if objectHierarchyAncestor.get('Name'):
                                        parentpath = objectHierarchyAncestor.get('Name') + ' / ' + parentpath
                        file1_name.append(parentpath + name)
        TkinterGUI.set_textlog(self, 'Etape 1/4')
        root.update()
        #Boucle iteration xml fichier 2
        for objectHierarchy in root_file2.iter('Object'):
                if objectHierarchy.get('Name') not in file2_name_check:
                        name = objectHierarchy.get('Name')
                        file2_name_check.append(name)
                        parentpath = ''
                        for objectHierarchyAncestor in list(objectHierarchy.iterancestors()):
                                if objectHierarchyAncestor.get('Name'):
                                        parentpath = objectHierarchyAncestor.get('Name') + ' / ' + parentpath
                        file2_name.append(parentpath + name)
        TkinterGUI.set_textlog(self, 'Etape 2/4')
        root.update()
        #Compare les differences et les écrits dans un fichier text 1->2
        logfile = open(pathresult1,"w+")
        name_diff = []
        for name_file1 in file1_name:
                check = False
                for name_file2 in file2_name:
                        if name_file1 == name_file2:
                                check = True
                if check == False:
                        name_diff.append(name_file1)
                        logfile.write(name_file1 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 3/4')
        root.update()
        #Compare les differences et les écrits dans un fichier text 2->1
        logfile = open(pathresult2,"w+")
        name_diff = []
        for name_file2 in file2_name:
                check = False
                for name_file1 in file1_name:
                        if name_file2 == name_file1:
                                check = True
                if check == False:
                        name_diff.append(name_file2)
                        logfile.write(name_file2 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 4/4')
        TkinterGUI.set_textlog(self, 'Comparaison terminé !')
        root.update()
    #fonction qui compare 2 fichier xml, 1 -> 2, créer 1 fichier text
    def compareXML_onlyName_1(self, file1, file2, directory_result, name_result1):
        TkinterGUI.set_textlog(self, 'Lancement du script !')
        root.update()
        #Init var
        root_file1 = et.parse(file1)
        root_file2 = et.parse(file2)
        pathresult1 = directory_result + "\\" + name_result1 + ".txt"
        file1_name = []
        file2_name = []
        name_diff = []
        #Boucle iteration xml fichier 1
        for objectHierarchy in root_file1.iter('Object'):
                if objectHierarchy.get('Name') not in file1_name:
                        file1_name.append(objectHierarchy.get('Name'))
        TkinterGUI.set_textlog(self, 'Etape 1/3')
        root.update()
        #Boucle iteration xml fichier 2
        for objectHierarchy in root_file2.iter('Object'):
                if objectHierarchy.get('Name') not in file2_name:
                        file2_name.append(objectHierarchy.get('Name'))
        TkinterGUI.set_textlog(self, 'Etape 2/3')
        root.update()
        logfile = open(pathresult1,"w+")
        #Compare les differences et les écrits dans un fichier text 1->2
        for name_file1 in file1_name:
                check = False
                for name_file2 in file2_name:
                        if name_file1 == name_file2:
                                check = True
                if check == False:
                        name_diff.append(name_file1)
                        logfile.write(name_file1 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 3/3')
        TkinterGUI.set_textlog(self, 'Comparaison terminé !')
        root.update()
    #fonction qui compare 2 fichier xml, 1 -> 2, 2->1, créer 2 fichier text
    def compareXML_onlyName_2(self, file1, file2, directory_result, name_result1, name_result2):
        TkinterGUI.set_textlog(self, 'Lancement du script !')
        root.update()
        #Init var
        root_file1 = et.parse(file1)
        root_file2 = et.parse(file2)
        pathresult1 = directory_result + "\\" + name_result1 + ".txt"
        pathresult2 = directory_result + "\\" + name_result2 + ".txt"
        file1_name = []
        file2_name = []
        name_diff = []
        #Boucle iteration xml fichier 1
        for objectHierarchy in root_file1.iter('Object'):
                if objectHierarchy.get('Name') not in file1_name:
                        file1_name.append(objectHierarchy.get('Name'))
        TkinterGUI.set_textlog(self, 'Etape 1/4')
        root.update()
        #Boucle iteration xml fichier 2
        for objectHierarchy in root_file2.iter('Object'):
                if objectHierarchy.get('Name') not in file2_name:
                        file2_name.append(objectHierarchy.get('Name'))
        TkinterGUI.set_textlog(self, 'Etape 2/4')
        root.update()
        #Compare les differences et les écrits dans un fichier text 1->2
        logfile = open(pathresult1,"w+")
        for name_file1 in file1_name:
                check = False
                for name_file2 in file2_name:
                        if name_file1 == name_file2:
                                check = True
                if check == False:
                        name_diff.append(name_file1)
                        logfile.write(name_file1 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 3/4')
        root.update()
        #Compare les differences et les écrits dans un fichier text 2->1
        logfile = open(pathresult2,"w+")
        for name_file2 in file2_name:
                check = False
                for name_file1 in file1_name:
                        if name_file2 == name_file1:
                                check = True
                if check == False:
                        name_diff.append(name_file2)
                        logfile.write(name_file2 + '\n')
        logfile.close()
        TkinterGUI.set_textlog(self, 'Etape 4/4')
        TkinterGUI.set_textlog(self, 'Comparaison terminé !')
        root.update()
    #
    # The meaning of this script is to call the script with prepared parameter
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    file1 = path + "\hierarchy_1_full.xml"
    file2 = path + "\hierarchy_2_full.xml"
    #print(file1)
    #print(file2)
    #subprocess.Popen(["python", "script.py","diff", file1, file2])

#Class de l'interface graphique Tkinter
class TkinterGUI:
    #fonction init de l'IHM
    def __init__(self, master):
        #Init Tkinter
        self.master = master
        master['bg']='white'
        master.geometry("900x400")
        master.resizable(width=False, height=False)
        master.title("CompareXML")
        #master.wm_iconbitmap('images.ico')
        #Init var
        self.path_file1 = StringVar()
        self.path_file2 = StringVar()
        self.name_result1 = StringVar(value='XML 1 compare to XML 2')
        self.name_result2 = StringVar(value='XML 2 compare to XML 1')
        self.path_directory = StringVar()
        self.script_selected = StringVar()
        self.hover = HoverInfo(self,'test de hover')
        #FRAME
        # frame 1 : Script list
        Frame_list = Frame(master, borderwidth=2, relief=GROOVE)
        label_list_1 =  Label(Frame_list, text = "Liste des scripts")
        scripts_options = ("Compare only name", "Compare name with path")
        self.script_selected.set(scripts_options[0])
        self.script_list = OptionMenu(Frame_list, self.script_selected, *scripts_options)
        self.script_selected.trace("w", self.get_infoScript)
        self.script_info = Text(Frame_list)
        #self.script_list = Listbox(Frame_list)
        #self.script_list.bind('<<ListboxSelect>>',self.get_infoScript)
        #self.script_list.insert(1,"Compare only name")
        #self.script_list.insert(2,"Compare name with path")

        # frame 2 : Main frame
        Frame_main = Frame(master, borderwidth=2, relief=GROOVE)
        label_1 = Label(Frame_main, text = "Fichier XML 1* : ")
        label_2 = Label(Frame_main, text = "Fichier XML 2* : ")
        label_3 = Label(Frame_main, text = "Repertoire de destination* : ")
        label_4 = Label(Frame_main, text = "Nom texte resultat : ")
        label_5 = Label(Frame_main, text = "Nom texte resultat : ")
        self.entry_pathfile1 = Entry(Frame_main, textvariable=self.path_file1, width=45)
        self.entry_pathfile2 = Entry(Frame_main, textvariable=self.path_file2, width=45)
        self.entry_nameresult1 = Entry(Frame_main, textvariable=self.name_result1, width=45)
        self.entry_nameresult2 = Entry(Frame_main, textvariable=self.name_result2, width=45)
        self.entry_nameresult1.bind("<Key>", self.checkunvalidchar)
        self.entry_nameresult2.bind("<Key>", self.checkunvalidchar)
        self.entry_pathdirectory = Entry(Frame_main, textvariable=self.path_directory, width=45)
        button_file1 = Button(Frame_main, text="Selectionner", command= lambda x=1:self.set_filename(1))
        button_file2 = Button(Frame_main, text="Selectionner", command= lambda x=1:self.set_filename(2))
        button_filedirectory = Button(Frame_main, text="Selectionner", command= lambda x=1:self.set_directory(1))
        self.checkBox = BooleanVar(value=True)
        self.chk_out2 = Checkbutton(Frame_main, text="Comparaison inverse", variable = self.checkBox, command = self.set_chk_result)
        button_startscript = Button(Frame_main, text="Lancer le script", command= lambda x=1:self.lauch_script(1))

        # frame 3 : Informations
        Frame_logs = Frame(master, bg="white", borderwidth=2, relief=GROOVE)
        self.scroll_log = Scrollbar(Frame_logs, orient="vertical")
        self.log_info = Text(Frame_logs, yscrollcommand = self.scroll_log.set)

        #LAYOUT
        #Frame List
        Frame_list.pack(side=LEFT)
        Frame_list.place(x = 0, y = 0, width = 300, height = 250)
        label_list_1.pack(padx=0, pady=0)
        self.script_list.pack(padx=0, pady=10, expand = True)
        self.script_info.pack(side=LEFT, expand=True, fill=BOTH)
        self.script_info.config(state=DISABLED)

        #Frame main
        Frame_main.pack(side=LEFT)
        Frame_main.place(x = 300, y = 0, width = 600, height = 250)
        label_1.grid(row=0, column=0, sticky=W, pady=5)
        label_2.grid(row=1, column=0, sticky=W, pady=5)
        label_3.grid(row=2, column=0, sticky=W, pady=5)
        label_4.grid(row=3, column=0, sticky=W, pady=5)
        label_5.grid(row=4, column=0, sticky=W, pady=5)
        self.entry_pathfile1.grid(row=0, column=1, sticky=W, pady=5)
        self.entry_pathfile2.grid(row=1, column=1, sticky=W, pady=5)
        self.entry_pathdirectory.grid(row=2, column=1, sticky=W, pady=5)
        button_file1.grid(row=0, column=2, sticky=W, padx=10, pady=5)
        button_file2.grid(row=1, column=2, sticky=W, padx=10, pady=5)
        button_filedirectory.grid(row=2, column=2, sticky=W, padx=10, pady=5)
        self.entry_nameresult1.grid(row=3, column=1, sticky=W, pady=5)
        self.entry_nameresult2.grid(row=4, column=1, sticky=W, pady=5)
        self.chk_out2.grid(row=4, column=2, sticky=W, padx=10, pady=5)
        button_startscript.grid(row=5, column=1, sticky=W, pady=5)

        #Frame Logs
        Frame_logs.pack(side=BOTTOM)
        Frame_logs.place(x = 0, y = 250, height=150, width = 900)
        self.log_info.pack(side=LEFT, expand = True, fill=BOTH)
        self.scroll_log.pack(side=RIGHT, fill=Y)
        self.scroll_log.config(command=self.log_info.yview)
        self.log_info.config(state=DISABLED)
    def get_selectedValue(self):
        #index = self.script_list.curselection()
        #if index:
        #    type_script = self.script_list.get(index)
        #else :
        #    type_script = "None"
        #return type_script
        return self.script_selected.get()
    #Ecrit du text dans le widget log_info
    def set_textlog(self, t):
        self.log_info.config(state=NORMAL)
        self.log_info.insert('end', t + '\n')
        self.log_info.config(state=DISABLED)
        self.log_info.see('end')
    def set_textscript(self, t):
        self.script_info.config(state=NORMAL)
        self.script_info.delete('1.0',END)
        self.script_info.insert('end', t + '\n')
        self.script_info.config(state=DISABLED)
        self.script_info.see('end')
    #lance le script séléctionner
    def lauch_script(self, t):
        if self.check_arguments():
            type_script = self.get_selectedValue()
            print(type_script)
            if type_script == "Compare name with path":
                if self.checkBox.get():
                    if os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True or os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True:
                        if messagebox.askyesno("Continuer ?", "Un ou plusieurs fichier existe déjà, voulez-vous les écraser ?"):
                            ScriptsXML.compareXML_withpath_2(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get(), self.entry_nameresult2.get())
                        else : self.set_textlog("Opération annulé")
                    else : ScriptsXML.compareXML_withpath_2(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get(), self.entry_nameresult2.get())
                elif os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True :
                        if messagebox.askyesno("Continuer ?", "Le fichier : " + self.entry_nameresult1.get() + " existe déjà, voulez vous l'écraser ?"): 
                            ScriptsXML.compareXML_withpath_1(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get())
                        else : self.set_textlog("Opération annulé")
                else: ScriptsXML.compareXML_withpath_1(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get())
            if type_script == "Compare only name":
                if self.checkBox.get():
                    if os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True or os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True:
                        if messagebox.askyesno("Continuer ?", "Un ou plusieurs fichier existe déjà, voulez-vous les écraser ?"):
                            ScriptsXML.compareXML_onlyName_2(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get(), self.entry_nameresult2.get())
                        else : self.set_textlog("Opération annulé")
                    else: ScriptsXML.compareXML_onlyName_2(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get(), self.entry_nameresult2.get())
                elif os.path.exists(self.entry_pathdirectory.get() + "\\" + self.entry_nameresult1.get() + ".txt") == True :
                        if messagebox.askyesno("Continuer ?", "Le fichier : " + self.entry_nameresult1.get() + " existe déjà, voulez vous l'écraser ?"):
                            ScriptsXML.compareXML_onlyName_1(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get())
                        else : self.set_textlog("Opération annulé")
                else : ScriptsXML.compareXML_onlyName_1(self, self.entry_pathfile1.get(), self.entry_pathfile2.get(), self.entry_pathdirectory.get(), self.entry_nameresult1.get())
            if type_script == "None":
                messagebox.showwarning("Selection Script", "Aucun script n'est selectionné")
        else : messagebox.showwarning("Information manquante", "Les champs * ne peuvent pas être vide")
    #Ecrit dans l'entry le chemin du document choisit
    def set_filename(self, i):
        filepath = filedialog.askopenfilename(filetypes=[("XML files","*.xml")])
        if i == 1:
            self.path_file1.set(filepath)
        elif i == 2:
            self.path_file2.set(filepath)
    #Ecrit dans l'entry le chemin du repertoir choisit
    def set_directory(self, i):
        filedirectory = filedialog.askdirectory()
        self.path_directory.set(filedirectory)
    #Check si l'option inverser est selectionne
    def set_chk_result(self):
        if self.checkBox.get():
            self.entry_nameresult2.config(state='normal')
        else: self.entry_nameresult2.config(state='disabled')
    def get_infoScript(self, *args):
        value=self.get_selectedValue()
        if value == "Compare name with path":
            #self.set_textlog("")
            self.set_textscript("Ce script compare les chemins avec les attributs Name des balises Object de deux fichiers XML")
            self.set_textscript("Le resultat est un fichier text avec les chemins des attributs Name non trouvé dans le fichier comparé")
        if value == "Compare only name":
            #self.set_textlog("")
            self.set_textscript("Ce script compare les attributs Name des balises Object de deux fichiers XML")
            self.set_textscript("Le resultat est un fichier text avec les attributs Name non trouvé dans le fichier comparé")
    #Fonction pour vérifier que tout les champs obligatoire soient remplis
    def check_arguments(self):
        test = True
        if len(self.entry_pathfile1.get()) == 0 or len(self.entry_pathfile2.get()) == 0 or len(self.entry_pathdirectory.get()) == 0:
            test = False
        return test
    #Check si le caractere taper est invalid, ouvre un popup pour avertire
    def checkunvalidchar(self, key):
        unsupportedchar = ['/', '\\', ':', '?', '<', '>', '|', '"']
        if key.char in unsupportedchar :
            messagebox.showwarning("Charactères invalide", 'Les charactères / \ : ? < > | " ne sont pas valide ')
#Lance l'application
root = Tk()
windows_app = TkinterGUI(root)
root.mainloop()
