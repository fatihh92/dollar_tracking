import locale
from colorama import Fore
from colorama import  init
from bs4 import BeautifulSoup
from urllib.request import  urlopen,Request
import time,datetime

def USD():
    url = "http://www.bloomberght.com/"
    url_oku = urlopen(Request(url))
    soup = BeautifulSoup(url_oku, 'html.parser')
    usd = soup.find_all("div", "line2")
    return usd[1].text.strip()



if __name__ == '__main__':
    init()
    locale.setlocale(locale.LC_ALL, 'tr-TR')

    while 1:
        try:
            dolar1 = USD()
            tt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            print(Fore.BLUE+"Dolar: "+str(USD())+" TRY -- ["+str(tt)+"]\n")
            time.sleep(60)
            dolar2 = USD()
            tt2 = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

            if dolar1 == dolar2:
                print(Fore.BLUE+"Dolar: "+str(dolar1)+" TRY -- ["+str(tt2)+"]\n")
            elif dolar1 > dolar2:
                az = locale.atof(dolar1) - locale.atof(dolar2)
                print(Fore.GREEN+"Dolar: "+str(dolar2)+" TRY -{0:.4f} ".format(az)+" -- ["+str(tt2)+"]\n")
            else:
                art = locale.atof(dolar2) - locale.atof(dolar1)
                print(Fore.RED+"Dolar: "+str(dolar2)+" TRY +{0:.4f} ".format(art)+" -- ["+str(tt2)+"]\n")

            answer = input("Continue..? (Y/y/N/n): ")
            if answer == 'Y' or answer == 'y':
                time.sleep(20)
                continue
            else:
                break
        except:
            print("Couldn't be successful")