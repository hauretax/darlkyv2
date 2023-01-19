import os
import bs4
from bs4 import BeautifulSoup
import requests
   
urls=[]



def readmeparse(url):
    r = requests.get(url, allow_redirects=True)
    open('readme', 'wb').write(r.content)
    with open('readme', 'r') as file:
        content = file.read()
        if "flag" in content:
            print('string exist in a file')
            print(url)
            print(content)

def scrape(site):
    r1 = requests.get(site)
    r2 = requests.get(site + "amcbevgondgcrloowluziypjdh/")
    r3 = requests.get(site + "amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/")
    s1 = BeautifulSoup(r1.text,"html.parser")
    s2 = BeautifulSoup(r2.text,"html.parser")
    s3 = BeautifulSoup(r3.text,"html.parser")
    basesite = site
    for i in s1.find_all("a"):
        href1 = i.attrs['href']
        site = basesite + href1

        if site not in  urls:
            urls.append(site) 
            if href1 == "README":
                readmeparse(site)
        for j in s2.find_all("a"):
            href2 = j.attrs['href']
            site = basesite + href1 + "/" + href2

            # print(site)
            if site not in  urls:
                urls.append(site) 
                if href2 == "README" and href1 != "README":
                    site = basesite + href1 + href2
                    readmeparse(site)
            for k in s3.find_all("a"):
                href3 = k.attrs['href']
                site = basesite + href1 + href2 + href3
                readmeparse(site + "/README")
                if site not in  urls:
                    urls.append(site) 
                    if href3 == "README" and href1 != "README" and href2 != "README":
                        readmeparse(site)
    
if __name__ =="__main__":
    site="http://192.168.59.4/.hidden/"
    scrape(site)
    print(len(urls))

# http://192.168.59.4/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw//README
# Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466