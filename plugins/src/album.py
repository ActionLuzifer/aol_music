import os
import track
import public_functions

class Album:
    '''
    /**
     * - Album enthält alle Informationen die zum einem Album dazugehören
     * - Album beherbergt auch die Funktionen zum Herunterladen der Datei und der anschließenden Konvertierung
     */
     pub_downloadTo( /path );
     pub_convert(); <-- mp3,cbr,192kbit IF this track was downloaded
     pub_tag();     <-- taggt die Datei IF this track was downloaded
    '''
    
    def __init__(self, mf_albumjson, mf_albumjsonFormatted):
        self._wasDownloaded = False;
        self.albumjson = mf_albumjson;
        self.m_albumjsonFormattedStr = mf_albumjsonFormatted
        self._album_art         = self.albumjson['cdlp']['album_art']; #"http:\/\/www.aolcdn.com\/music_lp\/wethe_sun204.jpg",
        self._album_name        = self.albumjson['cdlp']['album_name']; #"Sunshine State of Mind",
        self._album_thumbnail   = self.albumjson['cdlp']['album_thumbnail']; #"http:\/\/www.aolcdn.com\/music_lp\/wethe_sun204.jpg",
        self._artist_name       = self.albumjson['cdlp']['artist_name']; #"We the Kings",
        self._artist_profile    = self.albumjson['cdlp']['artist_profile']; #null
        self._ch_id             = self.albumjson['cdlp']['ch_id']; #"12625",
        self._commerce          = self.albumjson['cdlp']['commerce']; #"http:\/\/itunes.apple.com\/us\/album\/sunshine-state-of-mind\/id444929978",
        self._copyright         = self.albumjson['cdlp']['copyright']; #null
        self._description       = self.albumjson['cdlp']['description']; #"Combining '80s power pop hooks and a bright Florida-born sound, this band's latest record is fresh-squeezed. ",
        self._label             = self.albumjson['cdlp']['label']; #"[object Object]",
        self._lyrics            = self.albumjson['cdlp']['lyrics']; #"http:\/\/www.metrolyrics.com\/we-the-kings-lyrics.html",
        self._playlist_id       = self.albumjson['cdlp']['playlist_id']; #"2741",
        self._release_date      = self.albumjson['cdlp']['release_date']; #"",
        self._sponsor           = self.albumjson['cdlp']['sponsor']; #null
        self._upc               = self.albumjson['cdlp']['upc']; #""
        self._count             = self.albumjson['count']; #10
        self._queueOfTrack      = [];
        self.priv_createTracks(self.albumjson['tracks']);
        
    def priv_createTracks(self, mf_tracksJSONobj):
        trackNr = 0;
        for jtrack in mf_tracksJSONobj:
            trackNr = trackNr+1;
            mytrack = track.Track(self, jtrack, trackNr);
            self._queueOfTrack.append(mytrack);

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
    
    def pub_downloadTo(self, mf_path, mf_really):
        # download json-file
        fileStr = public_functions.f_getOSFilenameStr("{}_-_{}_-_".format(self.getartist_name(), self.getalbum_name()))
        myfileName = os.path.normpath("{0}/{1}00.json".format(mf_path, fileStr))
        myfile = open(myfileName, 'w')
        myfile.write(self.m_albumjsonFormattedStr)
        myfile.close()
        # kopiere Cover
        myCoverName = os.path.normpath("{0}/{1}00.jpg".format(mf_path, fileStr))
        myCover = open(myCoverName, 'wb')
        myCover.write(public_functions.f_urlToStringData(self.getalbum_thumbnail()))
        myCover.close()
        
        for mytrack in self._queueOfTrack:
            trackfileStr = public_functions.f_getOSFilenameStr(fileStr + "{:0>2}_-_{}".format(mytrack.m_trackNr, mytrack.m_title))
            mytrack.pub_downloadTo(mf_path, mf_really, trackfileStr+".flv");
            public_functions.f_transcode(mf_path, trackfileStr, ".flv", ".mp3")
            public_functions.f_removeFile(mf_path, trackfileStr + ".flv")
            public_functions.f_tagmp3File(os.path.normpath("{0}/{1}.mp3".format(mf_path, trackfileStr)),
                                          self._album_name, self._release_date, self._artist_name, mytrack.pub_get_tracknr(), mytrack.pub_get_tracktitle())
