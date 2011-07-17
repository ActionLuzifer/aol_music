import urllib
import json

class Album:
    '''
    /**
     * - Album enthält alle Informationen die zum einem Album dazugehören
     * - Album beherbergt auch die Funktionen zum Herunterladen der Datei und der anschließenden Konvertierung
     */
     downloadTo( /path );
     convert(); <-- mp3,cbr,192kbit IF this track was downloaded
     tag();     <-- taggt die Datei IF this track was downloaded
    '''
    
    def __init__(self, f_albumjson):
        self._wasDownloaded = False;
        self.albumjson = f_albumjson;
        self._album_art         = ""; #"http:\/\/www.aolcdn.com\/music_lp\/wethe_sun204.jpg",
        self._album_name        = ""; #"Sunshine State of Mind",
        self._album_thumbnail   = ""; #"http:\/\/www.aolcdn.com\/music_lp\/wethe_sun204.jpg",
        self._artist_name       = ""; #"We the Kings",
        self._artist_profile    = ""; #null
        self._ch_id             = ""; #"12625",
        self._commerce          = ""; #"http:\/\/itunes.apple.com\/us\/album\/sunshine-state-of-mind\/id444929978",
        self._copyright         = ""; #null
        self._description       = ""; #"Combining '80s power pop hooks and a bright Florida-born sound, this band's latest record is fresh-squeezed. ",
        self._label             = ""; #"[object Object]",
        self._lyrics            = ""; #"http:\/\/www.metrolyrics.com\/we-the-kings-lyrics.html",
        self._playlist_id       = ""; #"2741",
        self._release_date      = ""; #"",
        self._sponsor           = ""; #null
        self._upc               = ""; #""
        self._count             = 0; #10
        self._queueOfTrack      = [];
        
    
    def getwasDownloaded(self):
        return self._wasDownloaded;
    
    def getalbum_art(self):
        return self._album_art;
        
    def getalbum_name(self):
        return self._album_name;
    
    def getalbum_thumbnail(self):
        return self._album_thumbnail;
    
    def getartist_name(self):
        return self._artist_name;
    
    def getartist_profile(self):
        return self._artist_profile;
    
    def getch_id(self):
        return self._ch_id;
    
    def getcommerce(self):
        return self._commerce;
    
    def getcopyright(self):
        return self._copyright;
    
    def getdescription(self):
        return self._description;
    
    def getlabel(self):
        return self._label;
    
    def getlyrics(self):
        return self._lyrics;
    
    def getplaylist_id(self):
        return self._playlist_id;
    
    def getrelease_date(self):
        return self._release_date;
    
    def getsponsor(self):
        return self._sponsor;
    
    def getupc(self):
        return self._upc;
    
    def getcount(self):
        return self._count;
    
    def setInformations(self, htmllink):
        html_str = urllib.request.urlopen(htmllink);