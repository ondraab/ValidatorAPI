import json
import urllib2
import Model


class ValidatorManager(Model.Model):
    """
    Class gets structure from web.
    """

    def __init__(self):
        Model.Model.__init__(self)
        self.error = ""
        self.protein_model_list = []
        self.downloaded_pdb = {}

    def error_check(self, pdb_id):
        """
        :param pdb_id: PDBid which will be downloaded
        :return: bool, True for Error, False for success
        """

        try:
            self.downloaded_pdb = json.load(urllib2.urlopen("https://webchemdev.ncbr.muni.cz/API/Validation/Protein/" + pdb_id))

        except urllib2.URLError:
            self.error = "Could not load page. Check your internet connection."
            return True

        if 'Error' in self.downloaded_pdb:
            self.error = self.downloaded_pdb['Error']
            return True


        elif self.downloaded_pdb['MotiveCount'] == 0:
            self.error = "No models to validate! Please use another molecule."
            return True

        else:
            return False

    def download_entry(self, pdb_id):

        """
        Method checks internet connection, downloads entry from web, cheks, if there is something to validate.
        :param pdb_id: PDBid which will be downloaded
        :return: List of models of given PDBid
        """

        for item, val in enumerate(self.downloaded_pdb["Models"]):
            pdb_entry = self.downloaded_pdb["Models"][item]
            self.protein_model_list.append(pdb_entry)

        protein_model = Model.Model.get_model_info(self, self.protein_model_list)
        Model.Model.get_residue(self, protein_model)
        #Residue.Residue.get_residue(self, self.protein_models)

        return self.protein_model_list



