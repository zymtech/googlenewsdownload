import pycurl
import hashlib
import datetime
import time
import os

#pip install pycurl

def md5(str):
    if isinstance(str,basestring):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''
def getnewoutputpath(url,outputpathfordownload):
    lang = os.path.split(outputpathfordownload)[-1]
    urlmd5 = md5(url)
    u = int(time.time())
    crawlertime = unicode((datetime.datetime.fromtimestamp(u))).replace('-','').replace(' ','').replace(':','')
    filename =crawlertime+'_'+lang+'_'+urlmd5+'.html'
    p = os.path.join(outputpathfordownload,filename)
    return p



def download(url,outputpath,proxytype,address,port,username,password):
    try:
        if not os.path.exists(os.path.split(outputpath)[0]):
            os.mkdir(os.path.split(outputpath)[0])
        f = open(outputpath, 'a')
    except IOError as e:
        print e
    c = pycurl.Curl()
    c.setopt(c.URL,url)
    c.setopt(c.WRITEDATA,f)
    c.setopt(c.FOLLOWLOCATION,1)
    if proxytype!='':
        if proxytype == "socks4":
            c.setopt(c.PROXYTYPE,c.PROXYTYPE_SOCKS4)
        elif proxytype == "socks5":
            c.setopt(c.PROXYTYPE,c.PROXYTYPE_SOCKS5)
        else:
            c.setopt(c.PROXYTYPE,c.PROXYTYPE_HTTP)

        c.setopt(c.PROXY,address)
        c.setopt(c.PROXYPORT,port)

        if username:
            c.setopt(c.PROXYUSERPWD,username,password)
    #if ipv6:
    #    c.setopt(c.IPRESOLVE,c.IPRESOLVE_WHATEVER)
    #else:
    #    c.setopt(c.IPRESOLVE,c.IPRESOLVE_V4)
    c.perform()
    if c.getinfo(c.HTTP_CODE) != 200:
        os.remove(f.name)
    print url + 'downloaded'
    c.close()
    f.close()
