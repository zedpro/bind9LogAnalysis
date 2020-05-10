#!/usr/bin/env python3.6

from config import *
import sys

from logprocessor import LogProcessor

"""
Usage
./bind9LogAnalysis [file_log_name]

file_log_name : nome del file di log da analizzare. Il nome non deve contenere slash iniziali 
                    Se non specificato utilizza il file di defaut
                    La directory dei log è indicata nel file config.py

"""


# region MAIN

logFileName = DEFAULT_LOG_FILE

#
# Leggiamo i parametri di input per sapere se è stato indicato il nome di un file
#
if len(sys.argv) > 1:
    logFileName = sys.argv[1]


#
# Cominciamo l'analisi del file di log
#
logProcessor = LogProcessor(logFileName)

logProcessor.analysis()



exit(0)

# endregion






