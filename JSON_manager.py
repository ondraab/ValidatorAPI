import json
import urllib2
from pprint import pprint
import sys


class JSONParser():

    ##Argument length validation##
    ##def ArgValid(self, arglen):
        ##if len(arglen) != 4:
            ##print "ERROR! PDBid has got 4 characters, you type ", len(arglen)
            ##sys.exit()



    ## Method for downloading PDB from database##
    def DownloadEntry(self, PDBid):


        ProteinModels = []



        ### Internet connection check##
        try:
            entry = urllib2.urlopen("http://webchemdev.ncbr.muni.cz/API/Validation/Protein/"+PDBid)
        except urllib2.URLError:
            print "Could not load page. Check your internet connection."
            sys.exit()




        ##Check Error PDBs##
        DownloadedEntry = json.load(entry)
        if 'Error' in DownloadedEntry:
            print "PDB not fount. It's not in the database."
            sys.exit()



        ##Check if it not empty PDB##
        elif DownloadedEntry["MotiveCount"] == 0:
            print "Motive Count = 0! Nothing to validate. Please use another molecule."
            sys.exit()



        else:
            for item, val in enumerate(DownloadedEntry["Models"]):
                PDBEntry = DownloadedEntry["Models"][item]
                ProteinModels.append(PDBEntry)


        return ProteinModels


