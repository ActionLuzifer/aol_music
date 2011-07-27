#!/usr/bin/python3

'''
Created on 26.07.2011

@author: actionluzifer
'''

# Importieren is immer wichtich
from PyQt4 import QtGui

# meine Klassen
import sys
sys.path.append("src");
sys.path.append("plugins");
sys.path.append("plugins/src");
import gui
import public_functions


if __name__ == '__main__':
    downloadpath = public_functions.f_checkForDownloadPath()
    imagepath = public_functions.f_checkForImagePath()
    pluginspath = public_functions.f_checkForPluginsPath()

    qapp = QtGui.QApplication(sys.argv);
    maingui = gui.GUI(downloadpath, imagepath, pluginspath)
    sys.exit(qapp.exec_()) 
