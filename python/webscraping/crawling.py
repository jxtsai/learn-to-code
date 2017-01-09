from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()

random.seed(datetime.datetime.new())

def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")
	return addressParts

def getRandomExternalLinks(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html)
	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getExternalLinks(startingPage)
		return getNextExternalLink(internalLinks[random.randit(0, len(internalLinks)-1)]
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink("http://oreilly.com")
	print("Random enxeral link is: " + externalLink)
	followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")



