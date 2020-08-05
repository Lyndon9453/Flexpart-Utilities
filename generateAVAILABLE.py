##!/usr/bin/env python

""" Generate AVAILABLE file for meteo files in METEO_DIR.
   AVAILABLE is written to METEO_DIR, so script can be called from anywhere.
   Only meteo files valid for METEO_PREFIX are included.
"""

import glob
import os
import sys

if len(sys.argv) >= 2:
    METEO_PREFIX = sys.argv[1]
else:
    print("Insert the prefix of the meteo files (characters before the datetime numbers)\n" \
          "You must insert the path where meteo files are, otherwise yo must execute this script\n" \
          "from the folder with meteo files.\n" \
          "Example of usage:\n" \
          "\t\tpython generateAVAILABLE.py --prefix --path\n"
          "\t\tpython generateAVAILABLE.py EApub /home/maxpower/flexpart/preprocess/wind_fields/\n"
          "Aborting Execution")
    sys.exit()

if len(sys.argv) >= 3:
    METEO_DIR = sys.argv[2]
    if os.path.isdir(METEO_DIR):
        os.chdir(METEO_DIR)
    else:
        print("\nDirectory does not exist.\n"
              "Aborting Execution")
        sys.exit()
else:
    METEO_DIR = "."

print ("Looking for METEO files with \"{}\" prefix in \"{}\" dir".format(METEO_PREFIX, os.getcwd()))
# Load all files and sort as in AVAILABLE
meteo_files = glob.glob(METEO_PREFIX + '*')
meteo_files.sort()

# Check if any meteo file exists
if not meteo_files:
    print("\nDirectory does not contain meteo files.\nPlease execute this script from"
          " the folder with meteo files or insert the path where meteo files are.\n"
          "Aborting Execution ")
    sys.exit()


try:
    "for LINUX's users"
    AVAILABLE = open(os.getcwd() + '/AVAILABLE', 'w')
except:
    "for WINDOWS's users"
    AVAILABLE = open(METEO_DIR + '\\AVAILABLE', 'w')

# AVAILABLE.write("-\n-\n-\n")
AVAILABLE.write(  """DATE     TIME        FILENAME             SPECIFICATIONS\
   \nYYYYMMDD HHMISS\
  \n________ ______      __________________    __________________\n""")
print("\nData to be write in AVAILABLE file:\n")
for meteo_file in meteo_files:
    date = meteo_file[len(METEO_PREFIX):len(METEO_PREFIX)+6]
    hour = meteo_file[len(METEO_PREFIX)+6:len(METEO_PREFIX)+8]
    name = meteo_file
    DATO = "20%s %s0000      %s      ON DISK\n" % (date, hour, name)
    AVAILABLE.write(DATO)
    print(DATO)

AVAILABLE.close()

print("AVAILABLE file created in %s.\nPress Enter to exit." % METEO_DIR)
input()
