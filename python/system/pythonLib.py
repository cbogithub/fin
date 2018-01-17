#!/usr/bin/env python
# -*- coding: utf-8 -*-

pythonversion = 2

if(pythonversion == 2):
    import ConfigParser as configparser
else:
    import configparser

import hashlib
import time
if(pythonversion == 2):
    import urllib, urllib2

    def createSign(params):
        message = urllib.urlencode(params)
        message = message.encode(encoding='UTF8')
        m = hashlib.md5()
        m.update(message)
        m.digest()
        sig = m.hexdigest()
        return sig

    def httpPost(url, params):
        postdata = urllib.urlencode(params)
        postdata = postdata.encode('utf-8')

        print("httpPost:")
        print(url)
        print(params)
        
        fp = urllib2.urlopen(url, postdata, timeout = 20)

        #debug
        print("url return:%d "% fp.getcode())
        
        if fp.getcode() != 200:
            raise Exception("httpPost failed, detail is:%d" % fp.getcode() )
            return None
        else:
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
            ##test
            print(mystr)
            return mystr 

    def browserPost(url, params):
        postdata = urllib.urlencode(params)
        postdata = postdata.encode('utf-8')

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }
        print("browserPost:")
        print(url)
        print(headers)
        print(params)        
        req = urllib2.Request(url=url,headers=headers)  

        fp = urllib2.urlopen(req, postdata, timeout = 20)

        #debug
       
        print("url return:%d "% fp.getcode())
        
        if fp.getcode() != 200:
            raise Exception("httpPost failed, detail is:%d" % fp.getcode() )
            return None
        else:
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
            ##test
            print(mystr)
            return mystr      

else:
    import urllib 
    import requests

    def createSign(params):
        message = urllib.parse.urlencode(params)
        message = message.encode(encoding='UTF8')
        m = hashlib.md5()
        m.update(message)
        m.digest()
        sig = m.hexdigest()
        return sig
            
    def httpPost(url, params):
        postdata = urllib.parse.urlencode(params)
        postdata = postdata.encode('utf-8')

        fp = urllib.request.urlopen(url, postdata, timeout = 20)
        if fp.status != 200:
            return None
        else:
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
            return mystr 

    def browserPost(url, params):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }

        postdata = urllib.parse.urlencode(params)
        postdata = postdata.encode('utf-8')
        response = requests.post(url, postdata, headers=headers, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("httpPost failed, detail is:%s" % response.text)
