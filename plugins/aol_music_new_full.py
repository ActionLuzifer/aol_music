# Importieren is immer wichtich
#<segments>
import sys
import re
import json

# meine Klassen
sys.path.append("src");
sys.path.append("../src");
import public_functions
import album
import gui_Album


def fgetAnzahlPlugins():
    return 3


class PLUGIN:
    
    def __init__(self, mf_whichPlugin, mf_gui, mf_downloadpath, mf_imagepath):
        self.whichPlugin  = mf_whichPlugin 
        self.plugin       = False
        self.gui          = mf_gui    
        self.downloadPath = mf_downloadpath
        self.imagepath    = mf_imagepath
        self.pluginNames  = {0: "AOL MUSIC_New Releases, Full CDs", 
                             1: "spinner",
                             2: "zona estreno"}
        self.pluginStrings= {0: "http://music.aol.com/new-releases-full-cds", 
                             1: "http://www.spinner.com/new-releases",
                             2: "http://musica.aol.com/zona-estreno"}


    def _fgetURL(self):
        return self.pluginStrings[self.whichPlugin]


    def fcreate(self):
        self.plugin = AOL_Music_NewFull(self.gui, self.downloadPath, self.imagepath, self.pluginStrings[self.whichPlugin]) 


    def fdestroy(self):
        if self.plugin:
            self.plugin.fdestroy()


    def fgetName(self):
        return self.pluginNames[self.whichPlugin]


    def fdownload(self, mf_widgets):
        if self.plugin:
            self.plugin.fdownload(mf_widgets)


class AOL_Music_NewFull:
    
    def __init__(self, mf_gui, mf_downloadpath, mf_imagepath, mf_url):
        self.gui          = mf_gui    
        self.downloadPath = mf_downloadpath
        self.imagepath    = mf_imagepath
        self.url          = mf_url
        self.gui.setWindowTitle('aol-musicLoader')
        self.maxWidth  = 0
        self.maxHeight = 0
        
        # 1. Website laden
        mainLink = self.url;
        html_str = public_functions.f_urlToString(mainLink);
        
        # 2. Anzahl der Alben feststellen
        anzahlAlben = 0;
        bigRE = "playlisturl=\"(?P<PlaylistUrl>\\S*)\"";
        REprogramm = re.compile(bigRE);
        html_str = html_str.split("\n");
        self.listOfAlben = [];
        self.listOfWidgets = []
        for line in html_str:
            try:
                line = line.strip();
                foundObject = REprogramm.search(line);
                if(foundObject):
                    anzahlAlben = anzahlAlben+1;
                    urlstr = foundObject.group("PlaylistUrl");
                    albumstr = public_functions.f_urlToString(urlstr);
                    albumstr = albumstr.replace("\/", "/");
                    albumjson = json.loads(albumstr);
                    albumjsonFormatted = json.dumps(albumjson, sort_keys=True, indent=4)
                    newalbum = album.Album(albumjson, albumjsonFormatted);
                    self.listOfAlben.append(newalbum);
                    self._fcreateWidgets(newalbum)
            except:
                exctype, value = sys.exc_info()[:2]
                print("ERROR@AOL_Music_NewFull::def __init__(self, mf_gui, mf_downloadpath, mf_imagepath, mf_url)")
                print("Typ:  "+exctype)
                print("Wert: "+value)

        self.gui.pub_addInhalte(self.listOfWidgets, self.maxWidth, self.maxHeight)


    def _fcreateWidgets(self, mf_album):
        albumWidget = gui_Album.AlbumGUI(self.gui,
                                         mf_album.getalbum_thumbnail(), 
                                         self.imagepath,
                                         mf_album.getartist_name(), 
                                         mf_album.getalbum_name(), 
                                         mf_album.getdescription(),
                                         mf_album)
        self.listOfWidgets.append(albumWidget)

        if(self.maxWidth < albumWidget.pub_getWidth()):
            self.maxWidth = albumWidget.pub_getWidth()
        if(self.maxHeight < albumWidget.pub_getHeight()):
            self.maxHeight = albumWidget.pub_getHeight()


    def fdestroy(self):
        for widget in self.listOfWidgets:
            widget.hide()
            widget.destroy()


    def fdownload(self, mf_widgets):
        for widget in mf_widgets:
            widget.m_album.pub_downloadTo(self.downloadPath, True)

