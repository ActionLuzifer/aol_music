import sys
import urllib.request

def pub_urlToStringData(url):
    return urllib.request.urlopen(url).read();

def pub_replaceBadChars(mf_executeStr):
    mf_executeStr = mf_executeStr.replace(" ", "_")
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
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        myfileArray = pub_getPathStrWithoutLaufwerk(mf_filenameStr)
        mf_filenameStr = myfileArray[0] + pub_replaceBadChars(myfileArray[1])
    return mf_filenameStr
