class Residue():
    ##Class, iterating gets specific information of given PDB#

    def __init__(self):
        self.main_res = []
        self.model_names_dict = {}


        self.temp_foreign_atoms = {}
        self.foreign_atoms = {}

        self.substitutions = {}
        self.name_mismatches = {}

        self.missing_atoms_list = []
        self.missing_atoms_dict = {}

        self.missing_rings = []
        self.chirality_mismatches = {}
        self.entry_name = []
        self.model_name = []
        self.motive_count = 0
        self.state_bool = True
        self.state = []
        self.entry_count = 0



    def get_property(self, property, property_dict, model_count):
        """
        Compare given property dict with original model names dict and returns dict with original model name
        :param property:
        :param property_dict:
        :param modelcount:
        :return:
        """

        for key in property:
            property_dict = model_count["ModelNames"][key]

        return property_dict

    def get_residue(self, protein_model):
        """
        Iterating over "Entries" in individual model.
        :param protein_model: individual protein model
        :return:
        """

        self.entry_name.append(protein_model["ModelName"])


        if protein_model["State"] == "Degenerate":
            self.state_bool = False


        else:
            self.state_bool = True

        self.state.append(protein_model["State"])

        self.main_res.append(protein_model["MainResidue"].split(" ", 3))


        #self.get_property(["Substitutions"], self.substitutions, protein_model[model_count])

        #self.get_property(current_entry["NameMismatches"], self.name_mismatches, protein_model[model_count])



        #for i in protein_model["MissingAtoms"]:
            #if i not in self.missing_atoms_list:
                #self.missing_atoms_list.append(i)
                #self.missing_atoms_dict[i] = self.model_names_dict[i]



        self.temp_foreign_atoms = protein_model["ForeignAtoms"]


        ##Add new key to a dict of foreign atoms##
        #for key, value in self.temp_foreign_atoms.iteritems():
            #self.foreign_atoms[self.get_property(protein_model["ForeignAtoms"], self.temp_foreign_atoms, protein_model[model_count])] = self.temp_foreign_atoms[key]





        self.chirality_mismatches = protein_model["ChiralityMismatches"]
        #self.missingAtoms.append(currentEntry["MissingAtoms"])
        self.missing_rings = protein_model["MissingRings"]
        #print self.missingAtoms
