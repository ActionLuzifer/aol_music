'''
Created on 27.07.2011

@author: actionluzifer
'''

from PyQt4 import QtGui
from PyQt4 import Qt


class PluginAction(QtGui.QAction):
    '''
    classdocs
    '''


    def __init__(self, mf_plugin, mf_gui):
        '''
        Constructor
        '''
        QtGui.QAction.__init__(self, mf_plugin.fgetName(), mf_gui)
        self.plugin = mf_plugin
        self.gui    = mf_gui
        self.connect(self, Qt.SIGNAL("triggered()"), self.fdoTrigger)


    def fdoTrigger(self):
        self.gui.fcreatePlugin(self.plugin)
