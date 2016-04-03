#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import urllib
import os
import json

import click

from download import download
from download import getnewoutputpath

@click.command()
@click.option('--infilepath',help='absolute path of keywords file in json format')
@click.option('--outfilepath',help='output path')
@click.option('--proxytype',default='',help='which type of proxy you want to use')
@click.option('--username',default=None,help='username of proxy server')
@click.option('--password',default=None,help='password')
@click.option('--address',default='',help='address of proxy server')
@click.option('--port',help='port of proxy server')

def main(infilepath,outfilepath,proxytype,address,port,username,password):
    with open(infilepath) as data_file:
        file = json.load(data_file,encoding = "utf-8")
        gspider_lang = file.keys()
        for lang in gspider_lang:
            outfilepathfordownload = os.path.join(outfilepath,lang)
            for num in range(len(file[lang])):
                for keyword in range(len(file[lang][num]['keywords'])):
                    if file[lang][num]['urlencode'] == True:
                        kwunencoded = file[lang][num]['keywords'][keyword].encode('utf-8')
                        kw = urllib.quote(kwunencoded)
                    else:
                        kw = file[lang][num]['keywords'][keyword].encode('utf-8')
                    url = file[lang][num]['url']+kw
                    try:
                        outputpath = getnewoutputpath(url, outfilepathfordownload)
                        download(url,outputpath,proxytype,address,port,username,password)
                        time.sleep(1)
                    except BaseException as e:
                        print e

if __name__=="__main__":
    try:
        main()
    except BaseException as e:
        print e