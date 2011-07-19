import sys
import math
from PyQt4 import QtGui
from PyQt4.QtCore import Qt


import gui_Album

class GUI:
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
            
        
    
    def __init__(self, mf_listOfAlben, mf_downloadPath, mf_imagePath):
        self.qapp = QtGui.QApplication(sys.argv);
        self.m_listOfAlben = mf_listOfAlben
        self.m_downloadPath = mf_downloadPath 
        self.m_imagepath = mf_imagePath
                
        self.m_anzahlAlben = self.m_listOfAlben.__len__()
        
        # maximale Anzahl der Zeilen und Spalten ermitteln 
        #  (durch das math.ceil wird sichergestellt,dass immer aufgerundet wird)
        self.maxRows = math.ceil(math.sqrt(self.m_anzahlAlben))
        self.aktColumn = -1;
        self.aktRow = 0;
        
        self.m_main_window = QtGui.QWidget()
        self.m_main_window.setWindowTitle('aol-musicLoader')
        self.m_gridLayout = QtGui.QGridLayout(self.m_main_window)
        #self.m_scrollbarVert = QtGui.QScrollBar(Qt.Vertical, self.m_gridLayout)
        #self.m_scrollbarHori = QtGui.QScrollBar(Qt.Horizontal, self.m_gridLayout)
        
        self.m_main_window.show()
        
        for album in self.m_listOfAlben:
                self.priv_setNextRowAndColumn()
                self.priv_createWidgets(album)
        
        sys.exit(self.qapp.exec_()) 


    def priv_createWidgets(self, mf_album):
        albumWidget = gui_Album.AlbumGUI(mf_album.getalbum_thumbnail(), 
                                         self.m_imagepath,
                                         mf_album.getartist_name(), 
                                         mf_album.getalbum_name(), 
                                         mf_album.getdescription(),
                                         self.m_main_window)
        albumWidget.show()
        
        self.m_gridLayout.addWidget(albumWidget, self.aktRow, self.aktColumn)
        
        w = albumWidget.pub_getWidth()
        h = albumWidget.pub_getHeight()
        if(self.m_gridLayout.columnMinimumWidth(self.aktColumn) < w):
            self.m_gridLayout.setColumnMinimumWidth(self.aktColumn, w)
            
        if(self.m_gridLayout.rowMinimumHeight(self.aktRow) < h):
            self.m_gridLayout.setRowMinimumHeight(self.aktRow, h) 
        


if __name__ == '__main__':
    listOfAlben =[]
    gui = GUI(listOfAlben, "")