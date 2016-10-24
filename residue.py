import JSON_manager
import sys


class RESIDUE():
    ##Class, iterating over "Entries" in models#


    def __init__(self):
        self.mainRes = []
        self.foreignAtoms = {}
        self.substitutions = {}
        self.nameMismatches = {}
        self.missingAtoms = []
        self.missingRings = []
        self.chiralityMismatches = {}
        self.modelName = ""
        self.motiveCount = 0



    def ModelParser(self, pdbid):
        entry = []
        download = JSON_manager.JSONParser()
        for index, model in enumerate(download.DownloadEntry(pdbid)):
            entry.append(model)
        return entry




    def ResParser(self, pdbid):

        res = self.ModelParser(pdbid)
        Entries = {}
        Entries["ModelName"] = res
        idx = 0
        index = 0
        usedstructure =  res[idx]["Entries"][index]




        for idx, entries in enumerate(res):
            #print  res.ModelParser()[idx]["Entries"]

            self.modelName = res[idx]["ModelName"]


            for index, value in enumerate(res[idx]["Entries"]):

                if res[idx]["Entries"][index]["State"] == "Degenerate":
                    print "Nothing to validate. Model is degenerated."


                else:
                    #print res.ModelParser()[idx]["Entries"][index]
                    self.mainRes = res[idx]["Entries"][index]["MainResidue"].split(" ", 3)
                    print self.mainRes



                    for key in res[idx]["Entries"][index]["ForeignAtoms"]:
                        self.foreignAtoms[key] = res[idx]["ModelNames"][key]
                        print self.foreignAtoms



                    for key in res[idx]["Entries"][index]["Substitutions"]:
                        self.substitutions[key] = res[idx]["ModelNames"][key]
                        print self.substitutions



                    for key in res[idx]["Entries"][index]["NameMismatches"]:
                        self.nameMismatches[key] = res[idx]["ModelNames"][key]
                        print self.nameMismatches





                    self.ChiralityMismatches = res[idx]["Entries"][index]["ChiralityMismatches"]
                    self.missingAtoms = res[idx]["Entries"][index]["MissingAtoms"]
                    #print self.missingAtoms
                    self.missingRings = res[idx]["Entries"][index]["MissingRings"]
