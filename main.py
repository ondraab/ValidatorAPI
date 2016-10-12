import JSON_parser
import sys
import argparse
import residue

print "ValidatorAPI - This program validates PDBs from ValidatorDB database\n"

##ArgParser##
parser = argparse.ArgumentParser()
parser.add_argument("pdbid", help = "PDB which you want validate")
args = parser.parse_args()
#print args.pdbid


download = JSON_parser.JSONParser()
res = dict
check = JSON_parser.JSONParser()
check.ArgValid(args.pdbid)
#download.DownloadEntry(args.pdbid)

#ResParse = models.models()
#ResParse.ModelParser()

ResParse = residue.residue()
ResParse.ResParser()


