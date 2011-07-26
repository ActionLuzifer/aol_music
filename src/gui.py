#!/usr/bin/python3

import math
from PyQt4 import QtGui
#from PyQt4 import QtCore
from PyQt4 import Qt

import gui_Album

class GUI(QtGui.QWidget):
    '''
    /**
     * - der sichtbare Teil der Applikation
     * - 
     */
     getSelectedAlben(self);
    '''


    def priv_goButtonClicked(self):
        for albumgui in self.albumToDownloadList:
            albumgui.m_album.pub_downloadTo(self.m_downloadPath, True)


    def pub_addAlbumToDownloadList(self, gui_album):
        self.albumToDownloadList.append(gui_album)


    def pub_removeAlbumFromDownloadList(self, gui_album):
        self.albumToDownloadList.remove(gui_album)
        
    
    def priv_setNextRowAndColumn(self):
        if(self.aktColumn == self.maxRows):
            self.aktRow = self.aktRow+1
            self.aktColumn = 0;
        else:
            self.aktColumn = self.aktColumn + 1

            
    def priv_arrangeAlben(self):
        ww = 0
        wh = 0
        aw = self.maxWidth
        ah = self.maxHeight
        for albenWidget in self.listOfAlbenWidgets:
            self.priv_setNextRowAndColumn()
            albenWidget.resize(self.maxWidth, self.maxHeight)
            wx = (self.maxWidth+3)*self.aktColumn
            wy = (self.maxHeight+3)*self.aktRow
            albenWidget.move(wx, wy);
            
            if(ww < wx+aw):
                ww = wx+aw
            if(wh < wy+ah):
                wh = wy+ah 
        self.scrollWidget.resize(ww, wh+30)
        
            
    def resizeEvent(self, ev):
        self.m_scrollArea.setGeometry(0,0,ev.size().width(), ev.size().height())

    
    def __init__(self, mf_listOfAlben, mf_downloadPath, mf_imagePath, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.albumToDownloadList = []
        self.m_listOfAlben = mf_listOfAlben
        self.m_downloadPath = mf_downloadPath 
        self.m_imagepath = mf_imagePath
                
        self.m_anzahlAlben = self.m_listOfAlben.__len__()
        
        # maximale Anzahl der Zeilen und Spalten ermitteln 
        #  (durch das math.ceil wird sichergestellt,dass immer aufgerundet wird)
        self.maxRows = math.ceil(math.sqrt(self.m_anzahlAlben))
        self.aktColumn = -1;
        self.aktRow = 0;
        self.maxHeight = 0;
        self.maxWidth = 0;
        
        self.setWindowTitle('aol-musicLoader')
        
        self.m_scrollArea = QtGui.QScrollArea(self)
        self.scrollWidget = QtGui.QWidget(self)
        self.m_scrollArea.setWidget(self.scrollWidget)
        self.m_scrollArea.show()
        self.scrollWidget.show()        
        self.show()
        self.resize(800,600)
        self.move(30,30)
        
        self.listOfAlbenWidgets = []
        for album in self.m_listOfAlben:
                self.priv_createWidgets(album)

        self.priv_arrangeAlben()
        self.goButton = Qt.QPushButton("Lade ausgewählte Alben", self.scrollWidget)
        self.goButton.move(0, self.scrollWidget.height()-20)
        self.goButton.resize(self.scrollWidget.width(), 20)
        self.connect(self.goButton, Qt.SIGNAL("clicked()"), self.priv_goButtonClicked)
        self.goButton.show()
                
                
    def priv_createWidgets(self, mf_album):
        albumWidget = gui_Album.AlbumGUI(mf_album.getalbum_thumbnail(), 
                                         self.m_imagepath,
                                         mf_album.getartist_name(), 
                                         mf_album.getalbum_name(), 
                                         mf_album.getdescription(),
                                         self,
                                         mf_album,
                                         self.scrollWidget)
        self.listOfAlbenWidgets.append(albumWidget)

        if(self.maxWidth < albumWidget.pub_getWidth()):
            self.maxWidth = albumWidget.pub_getWidth()
        if(self.maxHeight < albumWidget.pub_getHeight()):
            self.maxHeight = albumWidget.pub_getHeight()
