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
    
    def __init__(self):
        __wasDownloaded = False;
        __title     = ""; #"Friday Is Forever",
        __url       = ""; #"http:\/\/serve.castfire.com\/audio\/653505\/friday-is-forever_2011-06-29-181705.cdlp.flv",
        __duration  = ""; #"184"
