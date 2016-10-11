import json
import urllib2
from pprint import pprint
import sys



class JSONParser():




    ##Argument length validation##
    def ArgValid(self, arglen):
        if len(arglen) != 4:
            print "ERROR! PDBid has got 4 characters, you type ", len(arglen)
            sys.exit()

    ## Method for downloading PDB from database##
    def DownloadEntry(self, PDBid, PDBJson):


        #def split_list(self, a_list):
            #half = len(a_list) / 2
            #return a_list[:half], a_list[half:]

        ##Internet connection check##
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
            result = {"Entry": sys.argv[1]}
            result["Models"] = [{}]
            modelList = []
            residues = []
            PDBJson = DownloadedEntry["Models"][0]["Entries"]
            # pprint(PDBJson)
            for item, val in enumerate(PDBJson):
                PDBEntry = PDBJson[item]
                #result["ModelName"] = PDBEntry["ModelName"]
                res = {}
                res["ModelName"] = PDBEntry["ModelName"]
                res["MainResidue"] = PDBEntry["MainResidue"]
                res["Residues"] = PDBEntry["Residues"]
                res["MissingAtoms"] = PDBEntry["MissingAtoms"]
                res["MissingRings"] = PDBEntry["MissingRings"]
                res["Substitutions"] = PDBEntry["Substitutions"]
                res["ChiralityMismatches"] = PDBEntry["ChiralityMismatches"]
                res["NameMismatches"] = PDBEntry["NameMismatches"]
                modelList.append(res)
                result["Models"] = modelList
                atomID = []
                ##Go through residues in all entries and make lists of atom IDs in each iteration
                for atom, id in enumerate(PDBEntry["Residues"]):
                    if len(PDBEntry["Residues"][atom]) == 7:
                        atomID.append(str(PDBEntry["Residues"][atom][0:3]))
                        atomID.append(int(PDBEntry["Residues"][atom][4:5]))
                        atomID.append(str(PDBEntry["Residues"][atom][6:7]))
                    elif len(PDBEntry["Residues"][atom]) == 8:
                        atomID.append(str(PDBEntry["Residues"][atom][0:3]))
                        atomID.append(int(PDBEntry["Residues"][atom][4:6]))
                        atomID.append(str(PDBEntry["Residues"][atom][7:8]))
                    elif len(PDBEntry["Residues"][atom]) == 9:
                        atomID.append(str(PDBEntry["Residues"][atom][0:3]))
                        atomID.append(int(PDBEntry["Residues"][atom][4:7]))
                        atomID.append(str(PDBEntry["Residues"][atom][8:9]))
                    #if len(atomID) > 3:
                        #residues.append(split_list(self, atomID))
                    #else:
                    #residues.append(atomID)
                    print atomID
            pprint(result)
            #pprint(residues)



