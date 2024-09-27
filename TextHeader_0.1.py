import numpy as np
import pandas as pd
import segyio
from segysak.segy import get_segy_texthead
from segysak.segy import create_default_texthead
from segysak.segy import put_segy_texthead
from segysak.segy import get_segy_texthead
import pathlib

''' ------------ Read SEGY file --------------------------'''
filename = "../DATA/0063_ESPIRITO_SANTO_39.0063-0100.STK_FIN.5.sgy"
filesegy = pathlib.Path(filename)
#print("PORRA", filesegy, filesegy.exists())

'''--------------Grab ebcdic header from Segy file --------'''

##ebcdic=get_segy_texthead(filesegy, ext_headers=False, no_richstr=False)
##print (ebcdic)

'''--------------Write ebcdic header to file ---------------'''

##Header = open("HEADER_GRAB", "w")
##Header.write(ebcdic)
##Header.close()

''' --------------Create a text header generic with overrides  (useless)---'''

#EBCDIC= create_default_texthead() #(override={7:'Hello', 8:'World!'})

''' --------------Read an EBCDIC file editted ------------------------------'''

Header = open("HEADER_GRAB", "r")
ebcdic=Header.read()
Header.close()

''' ---------------Writing into a header EBCDIC  into a Segy file -----------'''

put_segy_texthead(filesegy, ebcdic)
print (get_segy_texthead(filesegy))
