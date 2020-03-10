from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import re

myUrl = "https://www.cnn.com/"

uClient = uReq(myUrl)

pageHtml = uClient.read()
uClient.close()

#HTML Parsing
pageSoup = soup(pageHtml, "html.parser")
articles = pageSoup.findAll("span",{"class":"cd__headline-text"})

len(articles)