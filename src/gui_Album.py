import sys
import os

from PyQt4 import QtGui

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
        print (thumpnailSplitstring.__len__())
        return thumpnailSplitstring[thumpnailSplitstring.__len__() - 1]

    def priv_checkImageExists(self, mf_thumpnailPath):
        return os.path.isfile(mf_thumpnailPath)
        
    def loadImageFromNet(self, mf_url, mf_imagePathAndName):
        os.system("wget "+mf_url+ " -O"+mf_imagePathAndName)
        
    def pub_getWidth(self):
        if(self.m_main_window):
            return self.m_main_window.width()
        else:
            return 0
    
    def pub_getHeight(self):
        if(self.m_main_window):
            return self.m_main_window.height()
        else:
            return 0
    
    def __init__(self, mf_thumpnailUrl, mf_imagePath, mf_artistName, mf_albumName, mf_description, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.m_thumpnailUrl = mf_thumpnailUrl 
        self.m_imagepath = mf_imagePath
        self.m_thumpnailName = self.priv_check4Image(mf_thumpnailUrl)
        print(self.m_thumpnailName)
        self.m_imagepathAndName = self.m_imagepath + "/" + self.m_thumpnailName
        if not(self.priv_checkImageExists(self.m_imagepathAndName)):
            self.loadImageFromNet(self.m_thumpnailUrl, self.m_imagepathAndName)

        self.m_main_window = self # self.window()
        mw = self.m_main_window
        
        # albumCover anzeigen
        self.m_pixmap = QtGui.QPixmap(self.m_imagepathAndName)
        self.m_imageWidget = QtGui.QLabel(self.m_main_window)
        self.m_imageWidget.setPixmap(self.m_pixmap)
        maxheight = self.m_pixmap.height()+100
        maxbreite = self.m_pixmap.width()
        
        # Artist anzeigen
        starthoehe = self.m_pixmap.height() + 2
        self.m_artistLabel = QtGui.QLabel(mf_artistName, mw)
        self.m_artistLabel.setGeometry(0, starthoehe, maxbreite, 15)
        starthoehe = starthoehe+17
        
        # Album anzeigen
        self.m_albumLabel = QtGui.QLabel(mf_albumName, mw)
        self.m_albumLabel.setGeometry(0, starthoehe, maxbreite, 15)
        starthoehe = starthoehe+17
        
        # Beschreibung anzeigen
        self.m_desciptionLabel = QtGui.QTextEdit(mf_description, mw)
        self.m_desciptionLabel.setReadOnly(True)
        self.m_desciptionLabel.setGeometry(0, starthoehe, maxbreite, maxheight-starthoehe)
        
        # Hauptfenster anzeigen
        self.m_main_window.resize(maxbreite, maxheight)
        self.m_main_window.show()

if __name__ == '__main__':
    qapp = QtGui.QApplication(sys.argv);
    thumpnailURL = "http://o.aolcdn.com/os/music/CD-Listening-Party/shaggy_summerinkingston204.jpg"
    imagesPath = priv_checkForDownloadPath()
    gui = AlbumGUI(thumpnailURL, imagesPath, "Shaggy", "Summer in Kingston", "The &#039;It Wasn&#039;t Me&#039; singer is ready for another comeback with this latest release inspired by Shaggy&#039;s affinity for Jamaican singers. ")
    sys.exit(qapp.exec_()) 