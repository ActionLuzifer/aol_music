#!/usr/bin/python3

# Importieren is immer wichtich
import subprocess
import sys
import os
import re
import json
import urllib.request
import album

def urlToString(url):
    htmldings = urllib.request.urlopen(url);
    htmldings = str(htmldings.read());
    bigRE = "b'(?P<wanted>.*)'";
    REprogramm = re.compile(bigRE);
    foundObject = REprogramm.search(htmldings);
    htmldings = foundObject.group("wanted")
    return htmldings;

# 1. Website laden
mainLink = "http://music.aol.com/new-releases-full-cds";
html_str = urlToString(mainLink);

# 2. Anzahl der Alben feststellen
anzahlAlben = 0;
bigRE = "playlisturl=\"(?P<PlaylistUrl>\\S*)\"";
REprogramm = re.compile(bigRE);
html_str = html_str.split("\\n");
listOfAlben = [];
for line in html_str:
    
    
  line = line.strip();
  foundObject = REprogramm.search(line);
  if(foundObject):
    anzahlAlben = anzahlAlben+1;
    albumstr = urlToString(foundObject.group("PlaylistUrl"));
    albumjson = json.loads(albumstr);
    newalbum = album.Album(albumjson);
    listOfAlben.append(newalbum);

print("Anzahl Alben:     %d" % (anzahlAlben));
print("Laenge der Liste: %d" % listOfAlben.__len__()); 
#print(outputstr);

# 3. Namen der Interpreten und Alben ermitteln (+ eventuell Links zum Cover)

# 4. Informationen von 3. anzeigen und Benutzer auswählen lassen

# 5. Links zu den ausgewählten Dateien ermitteln

# 6. Dateien konvertieren
