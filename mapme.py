'''
Quickly pull up Google Maps directions for a given location. Idea originated here: https://automatetheboringstuff.com/chapter11/
'''

import webbrowser, sys, pyperclip

initialprompt = raw_input("Are you starting from Mapfre Stadium? y/n ")

if initialprompt == 'y':
    startingaddress = "One Black & Gold Blvd, Columbus, OH"
elif initialprompt == 'n':
    startingaddress = raw_input("What's the address you're starting from? " )

if pyperclip.paste() != '':
    if pyperclip.paste().isdigit():
        address = pyperclip.paste()
    else:
        address = raw_input("Please enter destination address. ")
else:
    address = raw_input("Please enter destination address. ")


webbrowser.open('https://www.google.com/maps/dir/' + startingaddress + '/' + address)


