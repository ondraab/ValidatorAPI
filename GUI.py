import Tkinter as tk
import ttk
import tkMessageBox
import residue


class MAINWINDOW(residue.RESIDUE):


    def __init__(self, master):

        residue.RESIDUE.__init__(self)

        self.master = master
        self.frame = tk.Frame(self.master)

        self.mainlabel = tk.Label(self.master, text="Validator", anchor=tk.W, font="Arial 12")
        self.mainlabel.grid(row=0, column=0)

        self.entrylabel = tk.Label(self.master, text="Put the PDBid you want to validate", anchor=tk.W)
        self.entrylabel.grid(row=1, column=0, sticky=tk.W)

        self.entry = tk.Entry(self.master, width=40)
        self.entry.grid(row=2, column=0, columnspan=1, sticky=tk.W)

        self.startbutton = tk.Button(self.master, text="Validate!", command=self.callvalidation)
        self.startbutton.grid(row=2, column=0)

        self.infobutton = tk.Button(self.master, text="Help", command=self.help)
        self.infobutton.grid(row=2, column=0, sticky=tk.E)

        self.box = ttk.Notebook(self.master, width=650, height=300)

        self.tab1 = tk.Frame(self.master)
        self.textbox1 = tk.Text(self.tab1)
        self.textbox1.grid(row=0, column=0)

        self.tab2 = tk.Frame(self.master)
        self.textbox2 = tk.Text(self.tab2)
        self.textbox2.grid(row=0, column=0)

        self.tab3 = tk.Frame(self.master)
        self.textbox3 = tk.Text(self.tab3)
        self.textbox3.grid(row=0, column=0)

        self.tab4 = tk.Frame(self.master)
        self.textbox4 = tk.Text(self.tab4)
        self.textbox4.grid(row=0, column=0)

        self.tab5 = tk.Frame(self.master)
        self.textbox5 = tk.Text(self.tab5)
        self.textbox5.grid(row=0, column=0)

        self.tab6 = tk.Frame(self.master)
        self.textbox6 = tk.Text(self.tab6)
        self.textbox6.grid(row=0, column=0)

        self.tab7 = tk.Frame(self.master)
        self.textbox7 = tk.Text(self.tab7)
        self.textbox7.grid(row=0, column=0)

        self.tab8 = tk.Frame(self.master)
        self.textbox8 = tk.Text(self.tab8)
        self.textbox8.grid(row=0, column=0)

        self.tab9 = tk.Frame(self.master)
        self.textbox9 = tk.Text(self.tab9)
        self.textbox9.grid(row=0, column=0)

        self.box.add(self.tab1, text="Main Info")
        self.box.add(self.tab2, text="Models")
        self.box.add(self.tab3, text="Residues")
        self.box.add(self.tab4, text="Foreign Atoms")
        self.box.add(self.tab5, text="Name Mismatches")
        self.box.add(self.tab6, text="Substitutions")
        self.box.add(self.tab7, text="Missing Atoms")
        self.box.add(self.tab8, text="Missing Rings")
        self.box.add(self.tab9, text="Chirality")

        self.box.grid(row=3)

    def help(self):
        infobox = tkMessageBox.showinfo("Help",
                                    "Validator\nType PDBid, which you want to validate and the program will give you information about all models  in given PDB")

    def callvalidation(self):
        #self.entry.get()
        residue.RESIDUE.ResParser(self, self.entry.get())

        self.textbox1.insert(tk.END, "PDBid: "+self.entry.get())
        self.textbox1.configure(state=tk.DISABLED)
        self.textbox1.update_idletasks()



        self.textbox2.insert(tk.END, self.modelName)
        self.textbox2.configure(state=tk.DISABLED)
        self.textbox2.update_idletasks()


        self.textbox3.insert(tk.END, self.mainRes)
        self.textbox3.configure(state=tk.DISABLED)
        self.textbox3.update_idletasks()


        self.textbox4.insert(tk.END, self.foreignAtoms)
        self.textbox4.configure(state = tk.DISABLED)
        self.textbox4.update_idletasks()



        self.textbox5.insert(tk.END, self.nameMismatches)
        self.textbox5.configure(state=tk.DISABLED)
        self.textbox5.update_idletasks()



        self.textbox6.insert(tk.END, self.substitutions)
        self.textbox6.configure(state=tk.DISABLED)
        self.textbox6.update_idletasks()



        self.textbox7.insert(tk.END, self.missingAtoms)
        self.textbox7.configure(state=tk.DISABLED)
        self.textbox7.update_idletasks()



        self.textbox8.insert(tk.END, self.missingRings)
        self.textbox8.configure(state=tk.DISABLED)
        self.textbox8.update_idletasks()




        self.textbox9.insert(tk.END, self.chiralityMismatches)
        self.textbox9.configure(state=tk.DISABLED)
        self.textbox9.update_idletasks()






def main():
    root = tk.Tk()
    root.wm_title("Validator")
    root.resizable(width=False, height=False)
    root.geometry("660x400")
    app = MAINWINDOW(root)
    root.mainloop()


if __name__ == '__main__':
    main()












