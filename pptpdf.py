import comtypes.client

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

PPTtoPDF(r'‪C:/Users/serhat/Desktop/Python Kod/BA6hafta.pptx','ss')

import sys  
import os  
import glob  
import comtypes.client  
  
def convert(files, formatType = 32):  
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")  
    powerpoint.Visible = 1  
    for filename in files:  
        newname = os.path.splitext(filename)[0] + ".pdf"  
        deck = powerpoint.Presentations.Open(filename)  
        deck.SaveAs(newname, formatType)  
        deck.Close()  
    powerpoint.Quit()  
  
files = glob.glob(r'mergtest') # <--- ONLY CHANGE  
convert(files)  