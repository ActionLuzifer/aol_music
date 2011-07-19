#!/usr/bin/python3

import math
from PyQt4 import QtGui

import gui_Album

class GUI(QtGui.QFrame):
    '''
    /**
     * - der sichtbare Teil der Applikation
     * - 
     */
     getSelectedAlben(self);
    '''

    
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
        self.scrollWidget.resize(ww, wh)
        
            
    def resizeEvent(self, ev):
        self.m_scrollArea.setGeometry(0,0,ev.size().width(), ev.size().height())

    
    def __init__(self, mf_listOfAlben, mf_downloadPath, mf_imagePath, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
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
        self.m_scrollArea.setGeometry(0,0, 800, 600)
        self.m_scrollArea.show()
        self.scrollWidget.setGeometry(0,0, 800, 600)
        self.scrollWidget.show()        
        
        self.show()
        
        self.listOfAlbenWidgets = []
        for album in self.m_listOfAlben:
                self.priv_createWidgets(album)

        self.priv_arrangeAlben()
        

    def priv_createWidgets(self, mf_album):
        albumWidget = gui_Album.AlbumGUI(mf_album.getalbum_thumbnail(), 
                                         self.m_imagepath,
                                         mf_album.getartist_name(), 
                                         mf_album.getalbum_name(), 
                                         mf_album.getdescription(),
                                         self.scrollWidget)
        self.listOfAlbenWidgets.append(albumWidget)

        if(self.maxWidth < albumWidget.pub_getWidth()):
            self.maxWidth = albumWidget.pub_getWidth()
        if(self.maxHeight < albumWidget.pub_getHeight()):
            self.maxHeight = albumWidget.pub_getHeight()


if __name__ == '__main__':
    listOfAlben =[]
    gui = GUI(listOfAlben, "")