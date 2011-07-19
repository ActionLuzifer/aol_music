import os

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

    def pub_downloadTo(self, mf_path, mf_really):
        fileStr = self.m_album.pub_replaceBadChars("{}_-_{}_-_{:0>2}_-_{}.flv".format(self.m_album.getartist_name(), self.m_album.getalbum_name(), self.m_trackNr, self.m_title))
        executeStr = "wget {} -O{}/".format(self.m_url, mf_path) + fileStr
        if mf_really :
            os.system(executeStr)
        else:
            print(executeStr)
        
