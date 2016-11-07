import json
import urllib2
import sys
import tkMessageBox


class JSON_MANAGER():
    """
        Class gets structure from web.
        """

    def __init__(self):
        self.proteinModels = []
        self.entry = {}






    def download_entry(self, PDBid):

        """
        Method checks internet connection, downloads entry from web, cheks, if there is something to validate.
        :param PDBid: PDBid which will be downloaded
        :return: Models of given PDBid
        """

        ### Internet connection check##
        try:
            urllib2.urlopen("https://webchemdev.ncbr.muni.cz/API/Validation/Protein/" + PDBid)
        except urllib2.URLError:
            tkMessageBox.showerror("Error", "Could not load page. Check your internet connection.")
            sys.exit()


        ##Check Error PDBs##
        self.entry = urllib2.urlopen("https://webchemdev.ncbr.muni.cz/API/Validation/Protein/" + PDBid)
        DownloadedEntry = json.load(self.entry)
        if 'Error' in DownloadedEntry:
            tkMessageBox.showerror("Error", DownloadedEntry["Error"])


        ##Check if it is not empty PDB##
        elif DownloadedEntry["MotiveCount"] == 0:
            tkMessageBox.showerror("Error", "Motive Count = 0! Nothing to validate. Please use another molecule.")
            print "Motive Count = 0! Nothing to validate. Please use another molecule."
            sys.exit()


        else:
            for item, val in enumerate(DownloadedEntry["Models"]):
                PDBEntry = DownloadedEntry["Models"][item]
                self.proteinModels.append(PDBEntry)

        return self.proteinModels