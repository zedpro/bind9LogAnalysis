
from config import *


class LogProcessor:

    def __init__(self, logFilename):

        self.logFilename = logFilename


    def analysis(self):
        """
        Analizza il file di log

        :return:
        """

        #
        # Componiamo path del file di log
        #
        logPath = '%s%s' % (LOG_DIR, self.logFilename)
        #
        # Apriamo il file e cominciamo a leggere il contenuto, riga per riga
        #
        with open(logPath) as f:

            for i, line in enumerate(f):

                print(line)


