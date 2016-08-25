'''
Quickly pull up Google Maps directions for a given location. Idea originated here: https://automatetheboringstuff.com/chapter11/
'''

import webbrowser, sys, pyperclip

startingaddress = "One Black & Gold Blvd, Columbus, OH"

if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
    # Use everything after [0] since that just contains the file name.
else:
    # Get the address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/dir/' + startingaddress + '/' + address)

