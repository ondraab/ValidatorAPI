import JSON_parser
import sys


class MODELS():
##Trida prochazejici jednotlive modely##
    def ModelParser(self):
        entry = []
        download = JSON_parser.JSONParser()
        for index, model in enumerate(download.DownloadEntry(sys.argv[1])):
            entry.append(model)
        return entry

