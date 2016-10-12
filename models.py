import JSON_parser
import sys


class MODELS():

    def ModelParser(self):
        download = JSON_parser.JSONParser()
        for index, val in enumerate(download.DownloadEntry(sys.argv[1])):
            print type(val)
        return val

