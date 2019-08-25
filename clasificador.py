#
#Hack Challenge
#

import re
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


#Crawler mercadolibre
def get_mercadolibre(busqueda):

    link ='https://listado.mercadolibre.com.mx/'
    busqueda = re.sub(' ','-',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "mercadolibre.sh" , link])
    return url.decode('utf-8').strip()

#Crawler coppel
def get_coppel(busqueda):
    link = "https://www.google.com.mx/search?q=coppel"
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "coppel.sh" , link])
    return url.decode('utf-8').strip()

#Crawler liverpool
def get_liverpool(busqueda):
    link = "https://www.google.com.mx/search?q=liverpool"
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "liverpool.sh" , link])
    return url.decode('utf-8').strip()

#Crawler amazon
def get_amazon(busqueda):
    link = "https://www.amazon.com.mx/s?k="
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "amazon.sh" , link])
    return url.decode('utf-8').strip()

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


def parseCoppel(url,browser):
	#descripción
	#tiempo de entrega
	#booleano para el cŕedito
	#tipo de crédito
	browser.get(url)
	html=browser.execute_script("return document.body.innerHTML")
	
	soup = BeautifulSoup(html,"lxml")
	
	coppel_name = soup.find("h1",{"class":"main_header"}).text
	coppel_price = soup.find("span",{"itemprop":"price"}).text


def parseMercadoLibre(soup):
	for h1 in soup.find_all('h1'):
		clases = h1.get('class')
		if clases != None:
			if "ui-pdp-title" in clases:
				mercadoLibre_name = h1.get_text('class')
				
	for span in soup.find_all('span'):
		clases = span.get('class')
		if clases != None:
			if "price-tag-fraction" in clases:
				mercadoLibre_price = span.get_text('class')
				
	for 
	return mercadoLibre_name, mercadoLibre_price	
	
def parseWalmart(url):	
	browser = webdriver.Firefox()
	browser.get(url)
	html=browser.execute_script("return document.body.innerHTML")
	
	soup = BeautifulSoup(html,"lxml")
	
	walmart_name = soup.find("h1",{"itemprop":"name"}).text
	walmart_price = soup.find("h4",{"itemprop":"price"}).text
		
	return walmart_name, walmart_price


empresas = ["coppel","walmart"]
productos = ["nintendo switch"]

competencia = {}

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
for producto in productos:
	for empresa in empresas:
		if empresa == "coppel":
			competencia["coppel"] = []
			url = get_coppel(producto)
			name,price = parseCoppel(url,browser)
			competencia["coppel"].append((name.strip(),price.strip()))
		
print(competencia)


#~ for html,archivo in zip(htmls,empresas):
	#~ soup = BeautifulSoup(html, 'html.parser')
	#~ if "elektra" in archivo:
		#~ competencia["elektra"] = []
		#~ name,price = parseElektra(soup)
		#~ competencia["elektra"].append((name.strip(),price.strip()))
	#~ elif "coppel" in archivo:
		#~ competencia["coppel"] = []
		#~ name,price = parseCoppel(soup)
		#~ competencia["coppel"].append((name.strip(),price.strip()))
	#~ elif "walmart" in archivo:
		#~ competencia["walmart"] = []
		#~ name,price = parseWalmart('https://www.walmart.com.mx/celulares/smartphones/celulares-desbloqueados/iphone-6s-apple-64-gb-space-gray-reacondicionado-desbloqueado_00071566070284')
		#~ competencia["walmart"].append((name.strip(),price.strip()))


