#!/usr/bin/python3

import math
from PyQt4 import QtGui
from PyQt4 import Qt

import os
import sys
sys.path.append("src")
sys.path.append("plugins")
sys.path.append("plugins/src")
import PluginAction
    

class GUI(QtGui.QWidget):
    '''
    /**
     * - der sichtbare Teil der Applikation
     * - 
     */
     getSelectedAlben(self);
    '''


    def __init__(self, mf_downloadPath, mf_imagePath, mf_pluginspath, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.doAResize = False
        self.oldPlugin = False
        self.albumToDownloadList = []
        self.listOfInhaltWidgets = []
        self.plugins = []
        self.anzahlInhalte = 0
        self.downloadPath = mf_downloadPath 
        self.imagePath = mf_imagePath
        self.pluginsPath = mf_pluginspath
                
        self.maxWidth  = 0
        self.maxHeight = 0
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollWidget = QtGui.QWidget(self)
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.show()
        self.scrollWidget.show()        
        self.move(30,30)
        self._fcreateMenus()
        self._fsearchForPlugins()
        
        self.goButton = Qt.QPushButton("Lade ausgewählte Inhalte", self.scrollWidget)
        self.connect(self.goButton, Qt.SIGNAL("clicked()"), self.priv_goButtonClicked)
        
        self.resize(800,600)
        self.show()
        


    def pub_arrageInhalteWidgets(self):
        self.priv_arrangeAlben()
        self.priv_arrangeDownloadButton()


    def priv_arrangeDownloadButton(self):
        self.goButton.move(0, self.scrollWidget.height()-20)
        self.goButton.resize(self.scrollArea.width()-20, 20)
        self.goButton.show()


    def pub_addInhalte(self, mf_content, mf_maxWidth, mf_maxHeight):
        self.listOfInhaltWidgets = mf_content
        self.anzahlInhalte = self.listOfInhaltWidgets.__len__()
        self.maxWidth  = mf_maxWidth
        self.maxHeight = mf_maxHeight


    def pub_getScrollWidget(self):
        return self.scrollWidget


    def priv_goButtonClicked(self):
        try:
            self.oldPlugin.fdownload(self.albumToDownloadList)
        except:
            exctype, value = sys.exc_info()[:2]
            print("ERROR@GUI::priv_goButtonClicked(self)")
            print("Typ:  "+exctype)
            print("Wert: "+value)


    def pub_addAlbumToDownloadList(self, gui_album):
        self.albumToDownloadList.append(gui_album)


    def pub_removeAlbumFromDownloadList(self, gui_album):
        self.albumToDownloadList.remove(gui_album)
        
    
    def priv_arrangeAlben(self):
        #TODO: event = [SCREEN.width, screen.height]
        self.resizeWindows(self.width(), self.height())


    def resizeEvent(self, ev):
        self.scrollArea.resize(ev.size().width(), ev.size().height()+20)
        self.resizeWindows(ev.size().width(), ev.size().height())
        self.priv_arrangeDownloadButton()
        
    
    def resizeWindows(self, windowWidth, windowHeight):
        if not (self.doAResize == True):
            self.doAResize = True
            x_column = 0
            max_x = 0
            y_row = 0
            space = 3
            maxHeightOfWidget = 0
            maxWidthOfWidget = 0
            
            for widget in self.listOfInhaltWidgets:
                widget.hide()
                if (windowWidth - x_column - widget.width()) > 0:
                    if maxHeightOfWidget < widget.height():
                        maxHeightOfWidget = widget.height()
                    if maxWidthOfWidget < widget.width():
                        maxWidthOfWidget = widget.width()
                else:
                    y_row = y_row + maxHeightOfWidget + space
                    if max_x < x_column:
                        max_x = x_column

                    x_column = 0
                    maxHeightOfWidget = widget.height()
                    maxWidthOfWidget = widget.width()
                    
                widget.move(x_column, y_row)
                widget.show()
                x_column = x_column + widget.width() + space

            if max_x < x_column:
                max_x = x_column
            self.scrollWidget.resize(max_x+maxWidthOfWidget, y_row + maxHeightOfWidget+21)
        self.doAResize = False


    def _fsearchForPlugins(self):
        files=os.listdir(self.pluginsPath)
        files=[filename for filename in files if filename.endswith("py")]
        files.remove("__init__.py")
        for file in files:
            file = file.replace(".py", "")
            pluginImport = __import__(file, globals(), locals(), [], 0)
            for xtesPlugins in range(pluginImport.fgetAnzahlPlugins()):
                plugin = pluginImport.PLUGIN(xtesPlugins, self, self.downloadPath, self.imagePath)
                self.plugins.append(plugin)
                self._fcreateActionAndMenu(plugin)


    def _fcreateActionAndMenu(self, mf_plugin):
        action = PluginAction.PluginAction(mf_plugin, self)
        self.menuPlugins.addAction(action)

    
    def fcreatePlugin(self, mf_plugin):
        # altes Plugin löschen
        if self.oldPlugin:
            for bla in range(self.albumToDownloadList.__len__()):
                self.albumToDownloadList.pop()
            self.oldPlugin.fdestroy()
        # neues Plugin erstellen
        self.oldPlugin = mf_plugin
        mf_plugin.fcreate()
        self.pub_arrageInhalteWidgets()


    def _fcreateMenus(self):
        self.menuBar = QtGui.QMenuBar(self)
        self.menuPlugins = self.menuBar.addMenu("&Plugins")
        self.testaction = QtGui.QAction("Test", self)
        self.connect(self.testaction, Qt.SIGNAL("triggered()"), self._ftest)
        self.menuBar.show()


    def _ftest(self):
        print("Test")