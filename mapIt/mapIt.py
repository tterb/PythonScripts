#!python3
# mapIt.py

###Description####################################################################
# This program opens a new google maps window in the user's default browser with
# the specified address, or the clipboard contents if an address is not specified
# via the command-line.
##################################################################################

import sys, webbrowser, pyperclip
googleMaps = "https://www.google.com/maps?saddr=My+Location&daddr="
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
webbrowser.open(googleMaps + address)
