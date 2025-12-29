#!/usr/bin/python3
import sys
import argparse
from src.schemes.scheme import Scheme

argparser = argparse.ArgumentParser(prog='convertJson2TrilinearForm.py',
                                description='Convert a Perminov json input file encoding a tensor to a trilianear output file')
argparser.add_argument('--json_file', help='the jsoninput file')
args = argparser.parse_args()

scheme = Scheme.load(args.json_file)
scheme.show_tensors()
