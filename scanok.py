# -*- coding: utf-8 -*-
#####################################
#        Pernah Waras               #
#    Code by h0d3_g4n               #
#   Telegram = @h0d3_g4n            #
#   ICQ = @h0d3_g4n                 #
#   Skype = live:f2c962ccea77ec0    #
#####################################
import requests, re, urllib2, os, sys, codecs, random, base64,json  
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time                 
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
biru = '\033[34m'
ungu = '\033[35m'
birumuda = '\033[36m'
grey = '\033[37m'
CEND = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    #'fcm-token': 'pelerganteng',
    'device': 'pelerganteng',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # 'Content-Length': '0',
}

#####################################
##########################################################################################
try:
        with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
                ooo = f.read().splitlines()
except IndexError:
        print (abang + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
        pass
ooo = list((ooo))
##########################################################################################
   
def scanners(url):
    try:
        get_jembut = requests.post(url+"/.git/config",headers=headers,timeout=15,verify=False)
        if 'repositoryformatversion =' in get_jembut.content or 'repositoryformatversion ="' in get_jembut.text:
            print ('Target: ' + url + ' ' +birumuda+ ':)' +ijo + ' Vuln !!'+ CEND)
            open('Vulns.txt','a').write(get_jembut.url.replace("/.git/config","")+"\n")
        else:
            print ('Target: ' + url + ' ' +birumuda+ ':(' +abang + ' Not Vuln !!' + CEND)
    except Exception as error:
        print(str(error))
        pass
    pass

#####################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 
 ___ ___ ___ __  _  __  _  _   _   _  __  ___  __   __  
| _,| __| _ |  \| |/  \| || | | | | |/  \| _ \/  \/' _/ 
| v_| _|| v | | ' | /\ | >< | | 'V' | /\ | v | /\ `._`. 
|_| |___|_|_|_|\__|_||_|_||_| !_/ \_|_||_|_|_|_||_|___/ 

            SCANNER 

             '''
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()

##########################################################################################
def Main():
        try:
                
                start = timer()
                ThreadPool = Pool(20)
                Threads = ThreadPool.map(scanners, ooo)
                print('TIME TAKE: ' + str(timer() - start) + ' S')
                
        except:
                pass


if __name__ == '__main__':
        Main()

