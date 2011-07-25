import os
import sys
import urllib.request

def pub_urlToStringData(url):
    return urllib.request.urlopen(url).read();

def pub_replaceBadChars(mf_executeStr):
    mf_executeStr = mf_executeStr.replace("/", "-")
    mf_executeStr = mf_executeStr.replace(":", "-")
    mf_executeStr = mf_executeStr.replace("?", "_")
    return mf_executeStr

def pub_getPathStrWithoutLaufwerk(mf_executeStr):
    firstStr = ""
    secondStr = mf_executeStr
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        firstStr = mf_executeStr[0:3]
        secondStr =  mf_executeStr[3:]
    return firstStr,secondStr

def pub_getOSFilenameStr(mf_filenameStr):
    mf_filenameStr = mf_filenameStr.replace(" ", "_")
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        myfileArray = pub_getPathStrWithoutLaufwerk(mf_filenameStr)
        mf_filenameStr = myfileArray[0] + pub_replaceBadChars(myfileArray[1])
    return mf_filenameStr

def pub_transcode(mf_path, mf_really, mf_trackfileStr, mf_fileEndingBefore, mf_fileEndingAfter):
    executeStr = "mplayer -dumpaudio -dumpfile \"{0}{1}\" \"{0}{2}\"".format(pub_getPath(mf_path, mf_trackfileStr), mf_fileEndingAfter, mf_fileEndingBefore)
    print(executeStr)
    os.system(executeStr)
    
def pub_getPath(mf_path, mf_file):
    return os.path.normpath("{0}/{1}".format(mf_path, mf_file))