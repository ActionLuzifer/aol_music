import urllib.request

def pub_urlToStringData(url):
    return urllib.request.urlopen(url).read();