import JSON_manager
import tkMessageBox



class RESIDUE():
    ##Class, iterating gets specific information of given PDB#



    def __init__(self):
        self.mainRes = []
        self.modelNames = {}


        self.tempForeignAtoms = {}
        self.foreignAtoms = {}

        self.substitutions = {}
        self.nameMismatches = {}

        self.missingAtomsList = []
        self.missingAtomsDict = {}

        self.missingRings = []
        self.chiralityMismatches = {}
        self.entryName = []
        self.modelName = []
        self.motiveCount = 0
        self.stateBool = True
        self.state = []
        self.entryCount = 0



    def get_model(self, pdbid):
        """
        Method iterating over Models, calls GETSTRUCTURE.downloadEntry method
        :param pdbid: valuated PDBid
        :return: individual model
        """

        entry = []
        download = JSON_manager.JSON_MANAGER()

        ##Main iteration cycle
        for index, model in enumerate(download.download_entry(pdbid)):
            entry.append(model)


        return entry

    def get_property(self, property, property_dict, modelcount):
        """

        :param property:
        :param property_dict:
        :param modelcount:
        :return:
        """

        for key in property:
            property_dict = modelcount["ModelNames"][key]

        return property_dict

    def get_residue(self, pdbid):
        """
        Iterating over "Entries" in individual models.
        :param pdbid: valuated PDB
        :return:
        """
        model = self.get_model(pdbid)
        entries = {}
        entries["ModelName"] = model

        for modelCount, modelKey in enumerate(model):
            # print  res.ModelParser()[idx]["Entries"]

            self.motiveCount += 1
            self.modelName.append(model[modelCount]["ModelName"])
            self.modelNames =model[modelCount]["ModelNames"]

            #Convert str key to int key
            self.modelNames = {int(k): v for k, v in self.modelNames.items()}

            for entryCount, entryKey in enumerate(model[modelCount]["Entries"]):
                self.entryCount += 1
                currentEntry = model[modelCount]["Entries"][entryCount]

                self.entryName.append(currentEntry["ModelName"])

                if currentEntry["State"] == "Degenerate":
                    self.stateBool = False
                    tkMessageBox.showwarning("Warning", "One or more model degenerated!")
                    break

                else:
                    self.stateBool = True

                self.state.append(currentEntry["State"])

                self.mainRes.append(currentEntry["MainResidue"].split(" ", 3))


                self.get_property(currentEntry["Substitutions"], self.substitutions, model[modelCount])

                self.get_property(currentEntry["NameMismatches"], self.nameMismatches, model[modelCount])



                for i in currentEntry["MissingAtoms"]:
                    if i not in self.missingAtomsList:
                        self.missingAtomsList.append(i)
                        self.missingAtomsDict[i] = self.modelNames[i]



                self.tempForeignAtoms = currentEntry["ForeignAtoms"]


                ##Add new key to a dict of foreign atoms##
                for key, value in self.tempForeignAtoms.iteritems():
                    self.foreignAtoms[self.get_property(currentEntry["ForeignAtoms"], self.tempForeignAtoms, model[modelCount])] = self.tempForeignAtoms[key]





                self.ChiralityMismatches = currentEntry["ChiralityMismatches"]
                #self.missingAtoms.append(currentEntry["MissingAtoms"])
                self.missingRings = currentEntry["MissingRings"]
                #print self.missingAtoms

    def get_res(self, pdbid, property, nameOfProperty):


        model = self.get_model(pdbid)

        for modelCount, modelKey in enumerate(model):
            self.motiveCount +=1
            self.modelName = model[modelCount]["ModelName"]

            for entryCount, entryKey in enumerate(model[modelCount]["Entries"]):
                self.entryCount += 1


                currentEntry = model[modelCount]["Entries"][entryCount]

                property = currentEntry[nameOfProperty]
                return property
