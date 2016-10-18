import models


class residue():
    ##Trida prochazejici jednotlive residua("Entries") v modelech##

    def __init__(self):
        self.mainRes = []
        self.foreignAtoms = {}
        self.substitutions = {}
        self.nameMismatches = {}
        self.missingAtoms = []
        self.missingRings = []


    def ResParser(self):
        res = models.MODELS()
        Entries = {}
        res.ModelParser()
        Entries["ModelName"] = res.ModelParser()
        for idx, entries in enumerate(res.ModelParser()):
            #print  res.ModelParser()[idx]["Entries"]
            for index, value in enumerate(res.ModelParser()[idx]["Entries"]):
                #print res.ModelParser()[idx]["Entries"][index]
                self.mainRes = res.ModelParser()[idx]["Entries"][index]["MainResidue"].split(" ", 3)
                print self.mainRes
                for key in res.ModelParser()[idx]["Entries"][index]["ForeignAtoms"]:
                    self.foreignAtoms[key] = res.ModelParser()[idx]["ModelNames"][key]
                    #print self.foreignAtoms
                for key in res.ModelParser()[idx]["Entries"][index]["Substitutions"]:
                    self.substitutions[key] = res.ModelParser()[idx]["ModelNames"][key]
                    #print self.substitutions
                for key in res.ModelParser()[idx]["Entries"][index]["NameMismatches"]:
                    self.nameMismatches[key] = res.ModelParser()[idx]["ModelNames"][key]
                    #print self.nameMismatches
                self.missingAtoms = res.ModelParser()[idx]["Entries"][index]["MissingAtoms"]
                #print self.missingAtoms
                self.missingRings = res.ModelParser()[idx]["Entries"][index]["MissingRings"]