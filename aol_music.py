#!/usr/bin/python3

# Importieren is immer wichtich
import subprocess
import sys
import os
import re
import json
import urllib.request

# meine Klassen
sys.path.append("src");
import album


def priv_urlToString(url):
    htmldings = urllib.request.urlopen(url);
    return str(htmldings.read().decode('utf-8'));

def priv_checkForPath():
    mypath = os.path.dirname("{0}".format(sys.argv[0])) + "/download";
    if not os.path.exists(mypath):
        os.system("mkdir {0}".format(mypath));
    return mypath;
        


# 1. Website laden
mainLink = "http://music.aol.com/new-releases-full-cds";
html_str = priv_urlToString(mainLink);

# 2. Anzahl der Alben feststellen
anzahlAlben = 0;
bigRE = "playlisturl=\"(?P<PlaylistUrl>\\S*)\"";
REprogramm = re.compile(bigRE);
html_str = html_str.split("\n");
listOfAlben = [];
for line in html_str:
  line = line.strip();
  foundObject = REprogramm.search(line);
  if(foundObject):
    anzahlAlben = anzahlAlben+1;
    urlstr = foundObject.group("PlaylistUrl");
    albumstr = priv_urlToString(urlstr);
    albumstr = albumstr.replace("\/", "/");
    albumjson = json.loads(albumstr);
    newalbum = album.Album(albumjson);
    listOfAlben.append(newalbum);

print("Anzahl Alben:     %d" % (anzahlAlben));
print("Laenge der Liste: %d" % listOfAlben.__len__()); 

#ALLE runterladen
downloadpath = priv_checkForPath();
for myalbum in listOfAlben:
    myalbum.pub_downloadTo(downloadpath, False);
# 6. Dateien konvertieren
