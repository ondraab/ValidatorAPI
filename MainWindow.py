import Tkinter as tk
import ttk
import tkMessageBox
import ValidatorManager



class MainWindow(ValidatorManager.ValidatorManager):


    def __init__(self, master):

        ValidatorManager.ValidatorManager.__init__(self)

        self.master = master
        self.frame = tk.Frame(self.master, borderwidth = 0)


        self.left_panel = ttk.Treeview(self.master, height = 19)
        self.left_panel.grid(row= 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
        self.left_panel.heading('#0', text = "PDBid")


        self.notebook = ttk.Notebook(self.master, width = 350, height = 390)
        self.notebook.grid(row= 0, column = 1, sticky = "nsew", columnspan = 15, padx = 5, pady = 5)


        self.tab_names = ['Entries', 'Missing', 'Name Mismatches', 'Chirality Mismatches', 'Foreign Atoms']


        self.entries_table = self.tab_maker(self.tab_names[0], ["Model Name", "State", "Main Residue"])
        self.missing_table = self.tab_maker(self.tab_names[1], ["Atoms", "Rings"])
        self.name_mismatches_table = self.tab_maker(self.tab_names[2], ["Model", "Motif"])
        self.chirality_mismatches_table = self.tab_maker(self.tab_names[3], ["Model", "Motif"])
        self.foreign_atoms_table = self.tab_maker(self.tab_names[4], ["Model", "Motif"])



        self.entry_label = tk.Label(self.master, text="Put the PDBid you want to validate", anchor=tk.W)
        self.entry_label.grid(row=1, column=0, sticky=tk.W, padx = 5)

        self.input_text = tk.StringVar()
        self.input_text.trace("w", lambda name, index, mode, sv=self.input_text: self.str_length(self.input_text))

        self.entry = tk.Entry(self.master, width=38, textvariable = self.input_text)
        self.entry.grid(row=2, column=0, sticky=tk.W, columnspan = 2, padx = 5, pady = 5)

        self.start_button = tk.Button(self.master, text="Validate!", command=lambda: self.start_validation())
        self.start_button.grid(row=2, column=1, sticky = tk.W, padx = 25, pady = 5)

        self.info_button = tk.Button(self.master, text="Help", command=self.help)
        self.info_button.grid(row=2, column=13, sticky=tk.E)


    def str_length(self, input_text):
        """
        Control length of given string.
        :param input_text: text written into entry box
        :return: True, if it has right length
        """
        c = self.input_text.get()[0:4]
        self.input_text.set(c)
        return True



    def add_option(self, pdb_id):
        """
        Method, makes a PDBid option in left panel + makes it's children (Models)
        :param pdb_id: given PDBid
        :return:
        """
        self.left_panel.insert("", 3, pdb_id, text=self.entry.get())
        for i in range(len(self.model_name_list)):
            self.left_panel.insert(pdb_id, 3, text= self.model_name_list[i])



    def help(self):
        """
        Run help window.
        :return:
        """
        tkMessageBox.showinfo("Help",
                                    "Validator\nType PDBid, which you want to validate and the program will give you information about all models  in given PDB")

    def tab_maker(self, tab,  column_names):
        """
        Method, makes tabs with given name
        :param name: name of tab
        :param columnames: name of columns for table
        :return:
        """
        self.tab = tk.Frame(self.master)

        self.tree = ttk.Treeview(self.tab, columns=column_names, height = 18)

        self.tree['show'] = 'headings'
        for i in range(len(column_names)):
            self.tree.heading(i, text=column_names[i])
            self.tree.column(i, stretch=tk.NO, width = 400/len(column_names))


        self.tree.grid(row = 0, columnspan = 4, sticky = "nsew", padx = 2, pady = 2)
        self.treeview = self.tree


        self.notebook.add(self.tab, text = tab)
        return self.treeview




    def start_validation(self):
        """
        Method, calls validation from RESIDUE class
        :return:
        """


        if ValidatorManager.ValidatorManager.error_check(self, self.entry.get()) == True:
            tkMessageBox.showerror("Error", self.error)
            return
        else:
            #ValidatorManager.ValidatorManager.__init__(self)
            self.downloaded_object = ValidatorManager.ValidatorManager.download_entry(self, self.entry.get())

            self.add_option(self.entry.get())


        for i in range(self.entry_count):
            self.entries_table.insert('', 'end', values = (self.main_res[i][0], self.state[i], self.main_res[i]))

        for key, value in enumerate(self.missing_atoms_dict):
            self.missing_table.insert('', 'end', values = (self.missing_atoms_dict[value]) )

        #for key, value in self.missing_atoms_dict.iteritems():
            #self.table4.insert('', 'end', values = (value))


        for key, value in self.foreign_atoms.iteritems():
            self.foreign_atoms_table.insert('', 'end', values = (key , value))


def main():
    root = tk.Tk()
    root.wm_title("Validator")
    root.resizable(width=False, height=False)
    root.geometry("640x480")
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
