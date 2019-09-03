import re
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://dmoz-odp.org/'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')
layers=list(page_soup.findAll("a",href=True))
#print(layers)
for i in range(0,len(layers)):
    a=re.sub(r'<a.+?href="', '', str(layers[i]).replace('</a>',''))
    a=re.sub(r'".+?">', '--',a)
    a=re.sub(r'<.+?>', '',a)
    if a.startswith('/'):
        b=my_url[0:len(my_url)-1]+a.replace('">','--')
        c=b.split('--')
        print(c[0])
    else:
        b=a.replace('">','--')
        c=b.split('--')
        print(c[0])
'''for i in range(1,len(players)):
    k=players[i].findAll("td",{"class":"cb-srs-stats-td"})
    #for j in range(len(k)):
    print("Name-"+k[0].text+"  /Matches-"+k[1].text+"   /Innings-"+k[2].text+"   /Runs-"+k[3].text+"   /Average-"+k[4].text)
#tendulkar=players[1]
#p=tendulkar.findAll("td",{"class":"cb-srs-stats-td"})
#print(p[1].text)
'''