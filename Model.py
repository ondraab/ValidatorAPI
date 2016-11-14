import Residue


class Model(Residue.Residue):
    def __init__(self):
        Residue.Residue.__init__(self)
        self.model_names_dict = {}
        self.motive_count = 0
        self.models = []
        self.model_name_list = []

    def get_model(self, protein_models):
        """
        Method, gets individual model from all given models.
        :param protein_models: List of all models
        :return: list of one model
        """
        individual_model = []
        for index, model in enumerate(protein_models):
            individual_model.append(model)
        return individual_model

    def get_model_info(self, protein_models):
        """
        Method, gets model proparties.
        :param protein_models: List of all models
        :return: individual_model
        """

        model = self.get_model(protein_models)

        for model_count, model_key in enumerate(model):
            self.motive_count += 1

            self.model_name_list.append(model[model_count]["ModelName"])
            self.model_names_dict = model[model_count]["ModelNames"]
            self.model_names_dict = {int(k): v for k, v in self.model_names_dict.items()}
        return model