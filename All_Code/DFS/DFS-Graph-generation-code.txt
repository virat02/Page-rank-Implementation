import requests
import pickle
from bs4 import BeautifulSoup

url_crawled = []
with open('urlsCrawledDFS.txt','r') as f:
   l = f.readlines()
l = [x.strip() for x in l]
url_crawled.extend(l)

d = {}
outlink = {}

def crawler(url):
    print(url)
    u = str(url).split('/wiki/')[1]
    outlink[u] = []
    r = requests.get(url)
    page_content = r.text
    soup = BeautifulSoup(page_content,"html.parser")
    for link in soup.find("div",{"id":"bodyContent"}).find_all('a'):
        href = "https://en.wikipedia.org" + str(link.get('href'))
        if href in url_crawled:
            outlink[u].append(str(href).split('/wiki/')[1])
            docId = str(link.get('href')).split('/wiki/')[1]
            if docId in d:
                if str(url).split('/wiki/')[1] not in d.get(docId):
                    d[docId].append(str(url).split('/wiki/')[1])
            else:
                d[docId] = [str(url).split('/wiki/')[1]]

for link in url_crawled:
    crawler(link)

#print(d)
def remove_duplicates(k,v):
    visited = []
    for a in v:
        if a not in visited:
            if not k == a:
                visited.append(a)
    return visited

url = {}
for key in d:
    url[key] = remove_duplicates(key,d[key])

olink = {}
for key in outlink:
    olink[key] = remove_duplicates(key,outlink[key])

f = open('urlsCrawledDFSInlinkGraph-new', 'w')
for key,value in url.items():
    f.write("\n%s " %key)
    f.write("%s " %value)
f.close()

f = open('urlsCrawledDFSOutlinkGraph-new', 'w')
for key,value in olink.items():
    f.write("\n%s " %key)
    f.write("%s " %value)
f.close()

with open("urlsCrawledDFSInlinkGraph-encoded.txt", 'wb') as f:
    pickle.dump(url,f)

with open("urlsCrawledDFSOutlinkGraph-encoded.txt", 'wb') as f:
    pickle.dump(olink,f)
