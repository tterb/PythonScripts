#!python3
# find.py

###Description####################################################################
# This program implements a simple command-line interface for using Everything
# Search Engine to search the user's machine for files featuring the provided string.
##################################################################################

import os, sys
if len(sys.argv) > 1:
    text = sys.argv[1:]
else:
    text = ''
print(os.system('Everything.exe -s' + text))
