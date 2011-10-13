import public_functions

class Track:
    '''
    /**
     * - Track enthält alle Informationen die ein einer Track benötigt
     * - Track beherbergt auch die Funktionen zum Herunterladen der Datei und der anschließenden Konvertierung
     */
     downloadTo( /path/and/filename);
     convert(); <-- mp3,cbr,192kbit IF this track was downloaded
     tag();     <-- taggt die Datei IF this track was downloaded
    '''
    
    def __init__(self, mf_album, mf_trackJSONobj, mf_trackNr):
        self.m_wasDownloaded = False;
        self.m_trackJSONobj  = mf_trackJSONobj;
        self.m_trackNr   = mf_trackNr;
        self.m_album     = mf_album;
        self.m_title     = self.m_trackJSONobj['title']; #"Friday Is Forever",
        self.m_url       = self.m_trackJSONobj['url']; #"http:\/\/serve.castfire.com\/audio\/653505\/friday-is-forever_2011-06-29-181705.cdlp.flv",
        self.m_duration  = self.m_trackJSONobj['duration']; #"184"


    def pub_downloadTo(self, mf_path, mf_really, fileStr):
        if mf_really :
            myTrackFile = open(public_functions.f_getPath(mf_path, fileStr), 'wb')
            myTrackFile.write(public_functions.f_urlToStringData(self.m_url))
            myTrackFile.close()
        else:
            print("{0} -> {1}/{2}".format(self.m_url, mf_path, fileStr))

    def pub_get_tracknr(self):
        return self.m_trackNr


    def pub_get_tracktitle(self):
        return self.m_title