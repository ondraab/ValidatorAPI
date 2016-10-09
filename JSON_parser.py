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
        #print json.dumps(result)
        #print result
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
            result = {"Protein": sys.argv[1]}
            result["Models"] = [{}]
            modelList = []
            #print result
            #print result["Models"][0]
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
                #pprint(result)
                #pprint(vysledek)
                ForeignAtomCount = PDBEntry["ForeignAtomCount"]
                ForeignAtoms = PDBEntry["ForeignAtoms"]
                SubstitutionCount = PDBEntry["SubstitutionCount"]
                Substitutions = PDBEntry["Substitutions"]
                ChiralityMismatchCount = PDBEntry["ChiralityMismatchCount"]
                ChiralityMismatches = PDBEntry["ChiralityMismatches"]
                #Id=PDBEntry["Id"]
                #print "Id", Id
                #print "ForeignAtomCount", ForeignAtomCount
                #print "ForeignAtoms", ForeignAtoms
                #print "SubstitutionCount", SubstitutionCount
                #print "Substitutions", Substitutions
                #print "ChiralityMismatchCount", ChiralityMismatchCount
                #print "ChiralityMismatches", ChiralityMismatches, "\n"

        pprint(modelList)


