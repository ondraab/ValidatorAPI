import Tkinter as tk
import ttk
import tkMessageBox
import ValidatorManager


class MainWindow():
    def __init__(self, master):


        self.master = master
        self.frame = tk.Frame(self.master, borderwidth=0)

        self.left_panel_frame = ttk.Notebook(self.master, height=390, width = 400)
        self.left_panel_frame.grid(row=0, column=0, pady=5, padx=(5, 5), columnspan=5)

        self.left_panel_table = ttk.Treeview(self.left_panel_frame, height=19)
        self.left_panel_table.grid(row=0, column=0, sticky="nsew", padx=5, pady=5, columnspan=5)
        self.left_panel_table.heading('#0', text="PDBid")
        self.left_panel_table.bind("<Button-1>", self.on_click_left_table)

        self.notebook = ttk.Notebook(self.master, width=350, height=390)
        self.notebook.grid(row=0, column=6, sticky="nsew", columnspan=6, pady=5)

        self.tab_names = ['Entries', 'Missing', 'Name Mismatches', 'Chirality Mismatches', 'Foreign Atoms']

        self.entries_table = self.tab_maker(self.tab_names[0], ["Missing Atoms", "Substitutions"], "Name")
        self.entries_table.bind("<Button-1>", self.on_click_entries_table)

        self.missing_table = self.tab_maker(self.tab_names[1], ["Atoms", "Rings"], "Name")

        self.name_mismatches_table = self.tab_maker(self.tab_names[2], ["Model", "Motif"], "Name")

        self.chirality_mismatches_table = self.tab_maker(self.tab_names[3], ["Model", "Motif"], "Name")

        self.foreign_atoms_table = self.tab_maker(self.tab_names[4], ["Model", "Motif"], "Name")

        self.entry_label = tk.Label(self.master, text="PDBid", anchor=tk.W)
        self.entry_label.grid(row=1, column=0, sticky=tk.NW, padx=(5, 2))

        self.input_text = tk.StringVar()
        self.input_text.trace("w", lambda name, index, mode, sv=self.input_text: self.str_length(self.input_text))

        self.entry = tk.Entry(self.master, width=18, textvariable=self.input_text)
        self.entry.grid(row=1, column=1, sticky=tk.NW, padx=(3, 5), columnspan=2)

        self.start_button = tk.Button(self.master, text="Validate!", command=lambda: self.start_validation())
        self.start_button.grid(row=1, column=3, sticky=tk.NW, padx=0)

        self.info_button = tk.Button(self.master, text="Help", command=self.help)
        self.info_button.grid(row=1, column=11, sticky=tk.NE)

        self.status_bar_frame = tk.Frame(self.master)
        self.status_bar_frame.configure(width=640, height=20)
        self.status_bar_frame.grid(column=0, columnspan=11)

        self.status_bar_label = tk.Label(self.status_bar_frame, text="Validator 1.0")
        self.status_bar_label.grid(sticky="w", column=0)

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
        try:
            self.left_panel_table.insert("", 1, pdb_id.lower(), text=pdb_id.lower())
            for i in self.downloaded_object.protein_model_list:
                self.left_panel_table.insert(pdb_id, 1, text=i["ModelName"])

        except tk.TclError:
            tkMessageBox.showerror("Error", "PDB already downloaded. Please use another molecule.")
            return




    def help(self):
        """
        Run help window.
        :return:
        """
        tkMessageBox.showinfo("Help",
                              "Validator\nType PDBid, which you want to validate and the program will give you information about all models  in given PDB")

    def tab_maker(self, tab, column_names, heading_column):
        """
        Method, makes tabs with given name
        :param name: name of tab
        :param columnames: name of columns for table
        :return:
        """
        self.tab = tk.Frame(self.master)

        self.tree = ttk.Treeview(self.tab, columns=column_names, height=18)

        #self.tree['show'] = 'headings'
        for i in range(len(column_names)):
            self.tree.heading(i, text=column_names[i])
            self.tree.column(i, stretch=tk.NO, width=400 / (len(column_names)+1))
        self.tree.heading('#0', text=heading_column)
        self.tree.column('#0', width = 400 / (len(column_names)+1))


        self.tree.grid(row=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        self.treeview = self.tree

        self.notebook.add(self.tab, text=tab)
        return self.treeview

    def on_click_left_table(self, event):
        clicked_item = self.left_panel_table.identify('item', event.x, event.y)

        if self.left_panel_table.parent(clicked_item) == '':
            return

        counter = 0

        pdb_id = self.left_panel_table.parent(clicked_item)
        model_index = self.left_panel_table.index(self.left_panel_table.identify('item', event.x, event.y))
        model_name = self.left_panel_table.item(clicked_item, "text")



        self.entries_table.delete(*self.entries_table.get_children())



        while model_name not in ValidatorManager.validation_report[pdb_id]["Models"][counter]["ModelName"]:
            counter +=1

        if model_name in ValidatorManager.validation_report[pdb_id]["Models"][counter]["ModelName"]:
            current_model = ValidatorManager.validation_report[pdb_id]["Models"][counter]["Entries"]

            for entry, properties in enumerate(current_model):
                    self.entries_table.insert('', 1, text = current_model[entry]["ModelName"], values = ( current_model[entry]["MissingAtomCount"], current_model[entry]["SubstitutionCount"]))


    def on_click_entries_table(self, event):
        clicked_item =  self.entries_table.identify('item', event.x, event.y)


    def start_validation(self):
        """
        Method, calls validation from RESIDUE class
        :return:
        """
        self.downloaded_object = ValidatorManager.ValidatorManager()

        if self.downloaded_object.error_check(self.entry.get()):
            tkMessageBox.showerror("Error", self.downloaded_object.error)
            return
        else:
            self.downloaded_object.download_entry(self.entry.get())
            self.add_option(self.entry.get())


            # for i in range(self.entry_count):
            # self.entries_table.insert('', 'end', values = (self.main_res[i][0], self.state[i], self.main_res[i]))

            # for key, value in enumerate(self.missing_atoms_dict):
            # self.missing_table.insert('', 'end', values = (self.missing_atoms_dict[value]) )

            # for key, value in self.missing_atoms_dict.iteritems():
            # self.table4.insert('', 'end', values = (value))


            # for key, value in self.foreign_atoms.iteritems():
            # self.foreign_atoms_table.insert('', 'end', values = (key , value))


def main():
    root = tk.Tk()
    root.wm_title("Validator")
    root.resizable(width=False, height=False)
    root.geometry("640x480")
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
