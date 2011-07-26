#!/usr/bin/python3
import sys
import os
import public_functions

from PyQt4 import QtGui
#from PyQt4 import QtCore

import gui

def priv_checkForDownloadPath():
    mypath = os.path.dirname("{0}".format(sys.argv[0])) + "/images";
    if not os.path.exists(mypath):
        os.system("mkdir {0}".format(mypath));
    return mypath;


class AlbumGUI(QtGui.QWidget):

    '''
    /**
     * - der sichtbare Teil der Applikation
     * - 
     */
     getSelectedAlben(self);
    '''
    
    
    def priv_check4Image(self, mf_thumpnailUrl):
        thumpnailSplitstring = mf_thumpnailUrl.split("/")
        return thumpnailSplitstring[thumpnailSplitstring.__len__() - 1]


    def priv_checkImageExists(self, mf_thumpnailPath):
        return os.path.isfile(mf_thumpnailPath)
        
        
    def loadImageFromNet(self, mf_url, mf_imagePathAndName):
        ImageFile = open(mf_imagePathAndName, 'wb')
        ImageFile.write(public_functions.pub_urlToStringData(mf_url))
        ImageFile.close()
        
        
    def pub_getWidth(self):
        return self.width()
        
        
    def pub_getHeight(self):
        return self.height()
        
    
    def mousePressEvent(self, event):
        if self.alreadyChosen:
            self.m_mainGUI.pub_removeAlbumFromDownloadList(self)
            self.alreadyChosen = False
            self.setPalette(self.m_pal_notChosen)
        else:
            self.m_mainGUI.pub_addAlbumToDownloadList(self)
            self.alreadyChosen = True
            self.setPalette(self.m_pal_chosen)
    
    
    def __init__(self, mf_thumpnailUrl, mf_imagePath, mf_artistName, mf_albumName, mf_description, mf_mainGUI, 
                 mf_album, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.m_thumpnailUrl = mf_thumpnailUrl 
        self.m_imagepath = mf_imagePath
        self.m_mainGUI = mf_mainGUI
        self.m_album   = mf_album
        self.alreadyChosen = False  
        self.m_thumpnailName = self.priv_check4Image(mf_thumpnailUrl)
        self.m_imagepathAndName = self.m_imagepath + "/" + self.m_thumpnailName
        if not(self.priv_checkImageExists(self.m_imagepathAndName)):
            self.loadImageFromNet(self.m_thumpnailUrl, self.m_imagepathAndName)
            
        self.m_col_chosen = QtGui.QColor(100,100,100);
        self.m_col_notChosen = QtGui.QColor(200,200,200);
        self.m_pal_chosen = QtGui.QPalette(self.m_col_chosen);
        self.m_pal_notChosen = QtGui.QPalette(self.m_col_notChosen);
        self.setPalette(self.m_pal_notChosen)
        
        # albumCover anzeigen
        self.m_pixmap = QtGui.QPixmap(self.m_imagepathAndName)
        self.m_imageWidget = QtGui.QLabel(self)
        self.m_imageWidget.setPixmap(self.m_pixmap)
        maxheight = self.m_pixmap.height()+100
        maxbreite = self.m_pixmap.width()
        
        # Artist anzeigen
        starthoehe = self.m_pixmap.height() + 2
        self.m_artistLabel = QtGui.QLabel(mf_artistName, self)
        self.m_artistLabel.setGeometry(0, starthoehe, maxbreite, 15)
        starthoehe = starthoehe+17
        
        # Album anzeigen
        self.m_albumLabel = QtGui.QLabel(mf_albumName, self)
        self.m_albumLabel.setGeometry(0, starthoehe, maxbreite, 15)
        starthoehe = starthoehe+17
        
        # Beschreibung anzeigen
        self.m_desciptionLabel = QtGui.QTextEdit(mf_description, self)
        self.m_desciptionLabel.setReadOnly(True)
        self.m_desciptionLabel.setGeometry(0, starthoehe, maxbreite, maxheight-starthoehe)
        
        # Hauptfenster anzeigen
        self.resize(maxbreite, maxheight)
        self.show()
