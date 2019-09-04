import re
import mysql.connector
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="atgworld",
    database="shubhang")
mycursor = mydb.cursor()
my_url='https://dmoz-odp.org/'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')
layers=list(page_soup.findAll("a",href=True))
#print(layers)
for i in range(15,63):
    a=re.sub(r'<a.+?href="', '', str(layers[i]).replace('</a>',''))
    a=re.sub(r'".+?">', '--',a)
    a=re.sub(r'<.+?>', '',a)
    if a.startswith('/'):
        b=my_url[0:len(my_url)-1]+a.replace('">','--')
        c=b.split('--')
        #mycursor.execute("INSERT INTO links_dmoz (hyperlink, hyperlink_title) VALUES('"+c[0]+"','"+c[1]+"')")
        #mydb.commit()
        print(c[0]+'---'+c[1])
    else:
        b=a.replace('">','--')
        c=b.split('--')
        #mycursor.execute("INSERT INTO links_dmoz (hyperlink, hyperlink_title) VALUES('"+c[0]+"','"+c[1]+"')")
        #mydb.commit()
        print(c[0]+'---'+c[1])
