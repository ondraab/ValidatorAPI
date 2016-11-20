import Residue


class Model():
    def __init__(self):
        self.model_names_dict = {}
        self.motive_count = 0
        self.model_name_list = []
        self.entries_list = []


    def get_model_info(self, model):
        """
        Method, gets model proparties.
        :param protein_models: List of all models
        :return: individual_model
        """

        self.model_name_list.append(model["ModelName"])
        self.model_names_dict = model["ModelNames"]
        self.model_names_dict = {int(k): v for k, v in self.model_names_dict.items()}

        for entry in model["Entries"]:
            self.entries_list.append(entry)
            Residue.Residue.get_residue(Residue.Residue(), entry)

        return model
