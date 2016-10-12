import models


class residue():
    def ResParser(self):
        res = models.MODELS()
        Entries = {}
        for idx, value in enumerate(res.ModelParser()):
            Entries["ModelName"] = res.ModelParser()["Entries"][0]
            print Entries
