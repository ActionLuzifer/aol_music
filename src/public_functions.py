import os
import sys
import urllib.request

def f_urlToStringData(url):
    return urllib.request.urlopen(url).read();

def f_replaceBadChars(mf_executeStr):
    mf_executeStr = mf_executeStr.replace(" ", "_")
    mf_executeStr = mf_executeStr.replace("/", "-")
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
