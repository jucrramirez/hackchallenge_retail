#
#Hack Challenge
#

from html.parser import HTMLParser
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from requests_html import HTMLSession
import asyncio


async def mmain():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://results.neptron.se/#/lundaloppet2018/?sortOrder=Place&raceId=99&page=0&pageSize=25')
    await page.screenshot({'path': 'pyppeteer_screenshot.png', 'fullPage': True})
    h4 = await page.querySelectorEval('h4', '(element) => element.outerHTML')
    print(h4)
    await browser.close()

#asyncio.get_event_loop().run_until_complete(mmain())

archivos = os.listdir("htmls")
htmls=[]
for archivo in archivos:
	with open("htmls/"+archivo) as entrada:
		htmls.append(entrada.read())

competencia = {}

def parseElektra(soup):
	for div in soup.find_all('div'):
		clases = div.get('class')
		if clases != None:
			if "productName" in clases:
				elektra_name = div.get_text('class')
				
	for strong in soup.find_all('strong'):
		strongs = strong.get('class')
		if strongs != None:
			if "skuBestPrice" in strongs:
				elektra_price = strong.get_text('class')	
	return elektra_name,elektra_price

def parseCoppel(soup):
	for h1 in soup.find_all('h1'):
		clases = h1.get('class')
		if clases != None:
			if "main_header" in clases:
				coppel_name = h1.get_text('class')
				
	for span in soup.find_all('span'):
		spans = span.get('itemprop')
		if spans != None:
			if "price" in spans:
				coppel_price = span.get_text('itemprop').split()[0]
	return coppel_name, coppel_price
	
def parseWalmart(url):	
	session = HTMLSession()
	r = session.get(url)
	r.html.render()
	table = r.html.find('h1[itemprop="name"]', first=False)
	for tabla in table:
		walmart_name = tabla.text
	table = r.html.find('h4[itemprop="price"]', first=False)
	for tabla in table:
		walmart_price = tabla.text		
	return walmart_name, walmart_price
	
for html,archivo in zip(htmls,archivos):
	soup = BeautifulSoup(html, 'html.parser')
	if "elektra" in archivo:
		competencia["elektra"] = []
		name,price = parseElektra(soup)
		competencia["elektra"].append((name.strip(),price.strip()))
	elif "coppel" in archivo:
		competencia["coppel"] = []
		name,price = parseCoppel(soup)
		competencia["coppel"].append((name.strip(),price.strip()))
	elif "walmart" in archivo:
		competencia["walmart"] = []
		name,price = parseWalmart('https://www.walmart.com.mx/celulares/smartphones/celulares-desbloqueados/iphone-6s-apple-64-gb-space-gray-reacondicionado-desbloqueado_00071566070284')
		competencia["walmart"].append((name.strip(),price.strip()))
			
print(competencia)		

#			print(elektra_name)
#	elektra_name = parseado.handle_starttag('div', [('class', 'productName')])
#	elktra_price = parseado.handle_starttag('strong', [('class', 'skuBestPrice')])
#	print(elektra_name)
#	print(elektra_price)
	#competencia[archivo[:-4]] = (nombre,precio)
		

#<strong class="skuBestPrice">$6,999.00</strong>

