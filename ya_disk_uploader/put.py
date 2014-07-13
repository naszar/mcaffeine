#!/usr/bin/python2

import pycurl,os,sys
from StringIO import StringIO

OAUTH_TOKEN = ''
false = False



def main():
#Get file for sending 
    try:
        out_filename = sys.argv[1]
    except:
        print "Say "+sys.argv[0]+" <filename> if you want upload <filename> to YandexDisk" 
        exit(1)
    else:
        try:
            out_file_fd = open(out_filename, 'rb')
        except IOError:
            print "file " + out_filename + " not found"
            exit(1)
        out_file_size = os.path.getsize(out_filename)
#get sending URL
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER,['Authorization: OAuth ' + OAUTH_TOKEN])
    c.setopt(pycurl.URL,"https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2F" + out_filename)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    result = c.getinfo(pycurl.RESPONSE_CODE)
    if result == 200:
        try:
            content = eval(storage.getvalue())
        except:
            print "Undifined error, server return ", storage.getvalue()
            exit(1)
        d=pycurl.Curl()
        d.setopt(pycurl.URL,content["href"])
        d.setopt(pycurl.HTTPHEADER,['Authorization: OAuth ' + OAUTH_TOKEN])
        d.setopt(pycurl.PUT,1)
        d.setopt(pycurl.READFUNCTION, out_file_fd.read)
        d.setopt(pycurl.INFILESIZE, out_file_size)
        d.perform()
        if d.getinfo(pycurl.RESPONSE_CODE) != 201:
            print d.getinfo(pycurl.RESPONSE_CODE), "Can't send error acrued" 
    else:
        print "Can't send error accrued"
        print "Server return", storage.getvalue()

if OAUTH_TOKEN != '':
    main()
else:
    print "Need for OAuth token (http://api.yandex.ru/disk/api/concepts/quickstart.xml)"
