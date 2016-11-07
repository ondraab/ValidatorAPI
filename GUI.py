import Tkinter as tk
import ttk
import tkMessageBox
import residue



class MAINWINDOW(residue.RESIDUE):


    def __init__(self, master):

        residue.RESIDUE.__init__(self)

        self.master = master
        self.frame = tk.Frame(self.master, borderwidth = 0)
        #self.frame.grid(sticky = "nsew", padx=10, pady= 20)



        self.notebook = ttk.Notebook(self.master, width = 600, height = 390)
        self.notebook.grid(row= 0, column = 0, sticky = "nsew", columnspan = 15, padx = 5, pady = 5)


        ##scrollbar = tk.Scrollbar(self.box)
        #scrollbar.grid(row=0, column=1, sticky=tk.E, rowspan=2)

        self.tab_names = ['Main Info', 'Models', 'Entries', 'Missing Atoms', 'Missing Rings', 'Name Mismatches', 'Chirality Mismatches', 'Foreign Atoms']


        self.table1 = self.tab_maker(self.tab_names[0], ["PDBID", "Number of models"])
        self.table2 = self.tab_maker(self.tab_names[1], ["Model Names"])
        self.table3 = self.tab_maker(self.tab_names[2], ["Model Name", "State", "Main Residue"])
        self.table4 = self.tab_maker(self.tab_names[3], ["Missing Atom"])
        self.table5 = self.tab_maker(self.tab_names[4], ["Missing Ring"])
        self.table6 = self.tab_maker(self.tab_names[5], ["Model", "Motif"])
        self.table7 = self.tab_maker(self.tab_names[6], ["Model", "Motif"])
        self.table8 = self.tab_maker(self.tab_names[7], ["Model", "Motif"])



        #self.tab_maker('Foreign Atoms')
        #self.tab_maker('Name Mismatches')
        #self.tab_maker('Substitutions')
        #self.tab_maker('Missing Atoms')
        #self.tab_maker('Missing Rings')
        #self.tab_maker('Chirality')


        self.entrylabel = tk.Label(self.master, text="Put the PDBid you want to validate", anchor=tk.W)
        self.entrylabel.grid(row=1, column=0, sticky=tk.W, padx = 5)

        self.input_text = tk.StringVar()
        self.input_text.trace("w", lambda name, index, mode, sv=self.input_text: self.str_length(self.input_text))

        self.entry = tk.Entry(self.master, width=38, textvariable = self.input_text, validatecommand = lambda: self.button_enabler(self.str_length(self.input_text), self.startbutton))
        self.entry.grid(row=2, column=0, sticky=tk.W, columnspan = 2, padx = 5, pady = 5)

        self.startbutton = tk.Button(self.master, text="Validate!", command=lambda: self.callvalidation())
        self.startbutton.grid(row=2, column=1, sticky = tk.W, padx = 25, pady = 5)

        self.infobutton = tk.Button(self.master, text="Help", command=self.help)
        self.infobutton.grid(row=2, column=13, sticky=tk.E)


    def str_length(self, input_text):
        c = self.input_text.get()[0:4]
        self.input_text.set(c)
        return True


    def help(self):
        """
        Run help window.
        :return:
        """
        infobox = tkMessageBox.showinfo("Help",
                                    "Validator\nType PDBid, which you want to validate and the program will give you information about all models  in given PDB")

    def tab_maker(self, tab,  columnames):
        """
        Method, makes tabs with given name
        :param name: name of tab
        :param columnames: name of columns for table
        :return:
        """
        self.tab = tk.Frame(self.master)

        self.tree = ttk.Treeview(self.tab, columns=columnames, height = 18)

        self.tree['show'] = 'headings'
        for i in range(len(columnames)):
            self.tree.heading(i, text=columnames[i])
            self.tree.column(i, stretch=tk.YES, width = 120)


        self.tree.grid(row = 0, columnspan = 4, sticky = "nsew", padx = 2, pady = 2)
        self.treeview = self.tree


        self.notebook.add(self.tab, text = tab)
        return self.treeview




    def callvalidation(self):
        """
        Method, calls validation from RESIDUE class
        :return:
        """

        #self.entry.get()
        residue.RESIDUE.get_residue(self, self.entry.get())

        self.table1.insert('', 'end', values = (self.entry.get(), self.motiveCount))

        for i in range(self.motiveCount):
            self.table2.insert('', 'end', values = (self.modelName[i]))

        for i in range(self.entryCount):
            self.table3.insert('', 'end', values = (self.mainRes[i][0], self.state[i], self.mainRes[i]))

        for key, value in self.missingAtomsDict.iteritems():
            self.table4.insert('', 'end', values = (value))


        for key, value in self.foreignAtoms.iteritems():
            self.table8.insert('', 'end', values = (key , value))



def main():
    root = tk.Tk()
    root.wm_title("Validator")
    #root.resizable(width=False, height=False)
    root.geometry("640x480")
    app = MAINWINDOW(root)
    root.mainloop()


if __name__ == '__main__':
    main()
