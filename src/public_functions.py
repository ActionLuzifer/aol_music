import os
import sys
import urllib.request
import stagger
from stagger.id3 import *       # contains ID3 frame types

def f_urlToStringData(url):
    return urllib.request.urlopen(url).read();

def f_replaceBadChars(mf_executeStr):
    mf_executeStr = mf_executeStr.replace(" ", "_")
    mf_executeStr = mf_executeStr.replace("&amp;", "&")
    mf_executeStr = mf_executeStr.replace("/", "-")
    mf_executeStr = mf_executeStr.replace("&#224;", "à"  )#     a mit accent grave (Gravis)     &agrave;     &#224;
    mf_executeStr = mf_executeStr.replace("&agrave;", "à")#     a mit accent grave (Gravis)     &agrave;     &#224;
    mf_executeStr = mf_executeStr.replace("&#225;", "á")  #     a mit accent aigu (Akut)     &aacute;     &#225;
    mf_executeStr = mf_executeStr.replace("&aacute;", "á")#     a mit accent aigu (Akut)     &aacute;     &#225;
    mf_executeStr = mf_executeStr.replace("&#226;", "â")  #     a mit Zirkumflex     &acirc;     &#226;
    mf_executeStr = mf_executeStr.replace("&acirc;", "â") #     a mit Zirkumflex     &acirc;     &#226;
    mf_executeStr = mf_executeStr.replace("&#227;", "ã")  #     a mit Tilde     &atilde;     &#227;
    mf_executeStr = mf_executeStr.replace("&atilde;", "ã")#     a mit Tilde     &atilde;     &#227;
    mf_executeStr = mf_executeStr.replace("&#228;", "ä")  #     a Umlaut     &auml;     &#228;
    mf_executeStr = mf_executeStr.replace("&auml;", "ä")  #     a Umlaut     &auml;     &#228;
    mf_executeStr = mf_executeStr.replace("&#229;", "å")  #     a mit Ring     &aring;     &#229;
    mf_executeStr = mf_executeStr.replace("&aring;", "å" )#     a mit Ring     &aring;     &#229;
    mf_executeStr = mf_executeStr.replace("&#230;", "æ")  #     a mit legiertem e     &aelig;     &#230;
    mf_executeStr = mf_executeStr.replace("&aelig;", "æ" )#     a mit legiertem e     &aelig;     &#230;
    mf_executeStr = mf_executeStr.replace("&#231;", "ç")  #     c mit Häkchen     &ccedil;     &#231;
    mf_executeStr = mf_executeStr.replace("&ccedil;", "ç")#     c mit Häkchen     &ccedil;     &#231;
    mf_executeStr = mf_executeStr.replace("&#232;", "è")  #     e mit accent grave (Gravis)     &egrave;     &#232;
    mf_executeStr = mf_executeStr.replace("&egrave;", "è")#     e mit accent grave (Gravis)     &egrave;     &#232;
    mf_executeStr = mf_executeStr.replace("&#233;", "é")  #     e mit accent aigu (Akut)     &eacute;     &#233;
    mf_executeStr = mf_executeStr.replace("&eacute;", "é")#     e mit accent aigu (Akut)     &eacute;     &#233;
    mf_executeStr = mf_executeStr.replace("&#234;", "ê")  #     e mit Zirkumflex     &ecirc;     &#234;
    mf_executeStr = mf_executeStr.replace("&ecirc;", "ê") #     e mit Zirkumflex     &ecirc;     &#234;
    mf_executeStr = mf_executeStr.replace("&#235;", "ë")  #     e Umlaut     &euml;     &#235;
    mf_executeStr = mf_executeStr.replace("&euml;", "ë")  #     e Umlaut     &euml;     &#235;
    mf_executeStr = mf_executeStr.replace("&#236;", "ì")  #     i mit accent grave (Gravis)     &igrave;     &#236;
    mf_executeStr = mf_executeStr.replace("&igrave;", "ì")#     i mit accent grave (Gravis)     &igrave;     &#236;
    mf_executeStr = mf_executeStr.replace("&#237;", "í")  #     i mit accent aigu (Akut)     &iacute;     &#237;
    mf_executeStr = mf_executeStr.replace("&iacute;", "í")#     i mit accent aigu (Akut)     &iacute;     &#237;
    mf_executeStr = mf_executeStr.replace("&#238;", "î")  #     i mit Zirkumflex     &icirc;     &#238;
    mf_executeStr = mf_executeStr.replace("&icirc;", "î") #     i mit Zirkumflex     &icirc;     &#238;
    mf_executeStr = mf_executeStr.replace("&#239;", "ï")  #     i Umlaut     &iuml;     &#239;
    mf_executeStr = mf_executeStr.replace("&iuml;", "ï")  #     i Umlaut     &iuml;     &#239;
    mf_executeStr = mf_executeStr.replace("&#240;", "ð")  #     kleines Eth (isländisch)     &eth;     &#240;
    mf_executeStr = mf_executeStr.replace("&eth;", "ð")   #     kleines Eth (isländisch)     &eth;     &#240;
    mf_executeStr = mf_executeStr.replace("&#241;", "ñ")  #     n mit Tilde     &ntilde;     &#241;
    mf_executeStr = mf_executeStr.replace("&ntilde;", "ñ")#     n mit Tilde     &ntilde;     &#241;
    mf_executeStr = mf_executeStr.replace("&#242;", "ò")  #     o mit accent grave (Gravis)     &ograve;     &#242;
    mf_executeStr = mf_executeStr.replace("&ograve;", "ò")#     o mit accent grave (Gravis)     &ograve;     &#242;
    mf_executeStr = mf_executeStr.replace("&#243;", "ó")  #     o mit accent aigu (Akut)     &oacute;     &#243;
    mf_executeStr = mf_executeStr.replace("&oacute;", "ó")#     o mit accent aigu (Akut)     &oacute;     &#243;
    mf_executeStr = mf_executeStr.replace("&#244;", "ô")  #     o mit Zirkumflex     &ocirc;     &#244;
    mf_executeStr = mf_executeStr.replace("&ocirc;", "ô") #     o mit Zirkumflex     &ocirc;     &#244;
    mf_executeStr = mf_executeStr.replace("&#245;", "õ")  #     o mit Tilde     &otilde;     &#245;
    mf_executeStr = mf_executeStr.replace("&otilde;", "õ")#     o mit Tilde     &otilde;     &#245;
    mf_executeStr = mf_executeStr.replace("&#246;", "ö")  #     o Umlaut     &ouml;     &#246;
    mf_executeStr = mf_executeStr.replace("&ouml;", "ö")  #     o Umlaut     &ouml;     &#246;
    mf_executeStr = mf_executeStr.replace("&#247;", "÷")  #     Divisions-Zeichen     &divide;     &#247;
    mf_executeStr = mf_executeStr.replace("&divide;", "÷")#     Divisions-Zeichen     &divide;     &#247;
    mf_executeStr = mf_executeStr.replace("&#248;", "ø")  #     o mit Schrägstrich     &oslash;     &#248;
    mf_executeStr = mf_executeStr.replace("&oslash;", "ø")#     o mit Schrägstrich     &oslash;     &#248;
    mf_executeStr = mf_executeStr.replace("&#249;", "ù")  #     u mit accent grave (Gravis)     &ugrave;     &#249;
    mf_executeStr = mf_executeStr.replace("&ugrave;", "ù")#     u mit accent grave (Gravis)     &ugrave;     &#249;
    mf_executeStr = mf_executeStr.replace("&#250;", "ú")  #     u mit accent aigu (Akut)     &uacute;     &#250;
    mf_executeStr = mf_executeStr.replace("&uacute;", "ú")#     u mit accent aigu (Akut)     &uacute;     &#250;
    mf_executeStr = mf_executeStr.replace("&#251;", "û")  #     u mit Zirkumflex     &ucirc;     &#251;
    mf_executeStr = mf_executeStr.replace("&ucirc;", "û") #     u mit Zirkumflex     &ucirc;     &#251;
    mf_executeStr = mf_executeStr.replace("&#252;", "ü")  #     u Umlaut     &uuml;     &#252;
    mf_executeStr = mf_executeStr.replace("&uuml;", "ü")  #     u Umlaut     &uuml;     &#252;
    mf_executeStr = mf_executeStr.replace("&#253;", "ý")  #     y mit accent aigu (Akut)     &yacute;     &#253;
    mf_executeStr = mf_executeStr.replace("&yacute;", "ý")#     y mit accent aigu (Akut)     &yacute;     &#253;
    mf_executeStr = mf_executeStr.replace("&#254;", "þ")  #     kleines Thorn (isländisch)     &thorn;     &#254;
    mf_executeStr = mf_executeStr.replace("&thorn;", "þ") #     kleines Thorn (isländisch)     &thorn;     &#254;
    mf_executeStr = mf_executeStr.replace("&#255;", "ÿ")  #     y Umlaut     &yuml;     &#255;
    mf_executeStr = mf_executeStr.replace("&yuml;", "ÿ")  #     y Umlaut     &yuml;     &#255;

    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        mf_executeStr = mf_executeStr.replace(":", "-")
        mf_executeStr = mf_executeStr.replace("?", "_")
    return mf_executeStr

def f_getPathStrWithoutLaufwerk(mf_executeStr):
    firstStr = ""
    secondStr = mf_executeStr
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        firstStr = mf_executeStr[0:3]
        secondStr =  mf_executeStr[3:]
    return firstStr,secondStr

def f_getOSFilenameStr(mf_filenameStr):
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        myfileArray = f_getPathStrWithoutLaufwerk(mf_filenameStr)
        mf_filenameStr = myfileArray[0] + f_replaceBadChars(myfileArray[1])
    else:
        mf_filenameStr = f_replaceBadChars(mf_filenameStr)
    return mf_filenameStr

def f_transcode(mf_path, mf_trackfileStr, mf_fileEndingBefore, mf_fileEndingAfter):
    executeStr = "mplayer -dumpaudio -dumpfile \"{0}{1}\" \"{0}{2}\"".format(f_getPath(mf_path, mf_trackfileStr), mf_fileEndingAfter, mf_fileEndingBefore)
    print(executeStr)
    os.system(executeStr)
    
def f_removeFile(mf_path, mf_trackfileStr):
    os.remove(f_getPath(mf_path, mf_trackfileStr))
    
def f_getPath(mf_path, mf_file):
    return os.path.normpath("{0}/{1}".format(mf_path, mf_file))

def f_checkForPath(mf_subPath):
    mypath = os.path.normpath("{0}".format(os.getcwd()) + mf_subPath)
    if not os.path.exists(mypath):
        os.system("mkdir {0}".format(mypath))
    return mypath

def f_checkForDownloadPath():
    return f_checkForPath("/download")
            
def f_checkForImagePath():
    return f_checkForPath("/images")

def f_checkForPluginsPath():
    return f_checkForPath("/plugins")

def f_urlToString(url):
    htmldings = urllib.request.urlopen(url);
    return str(htmldings.read().decode('utf-8'));


def f_tagmp3File(filename, artist, year, album, tracknr, tracktitle):
    print("TODO: TEST-TAGGING")
    tag24 = stagger.Tag24()
    print("filename   : "+filename)
    print("artist     : "+artist)
    tag24.artist = artist
    print("year       : "+year)
    tag24.date = year
    print("album      : "+album)
    tag24.album=album
    print("tracknr    : {:0>2}".format(repr(tracknr)))
    tag24.track = tracknr
    print("tracktitle : "+tracktitle)
    tag24.title = tracktitle
    tag24.write(filename)
