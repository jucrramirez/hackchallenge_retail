#
#Hack Challenge
#

import re
from bs4 import BeautifulSoup

import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Crawler elektra
def get_elektra(busqueda):

    link ='https://www.elektra.com.mx/'
    busqueda = re.sub(' ','%20',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "elektra.sh" , link])
    return url.decode('utf-8').strip()


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

def parseElektra(url,browser):
	browser.get(url)
	html = browser.execute_script("return document.body.innerHTML")
	
	soup = BeautifulSoup(html,"lxml")
	
	elektra_name = soup.find("div",{"class":"productName"}).text
	elektra_price = soup.find("strong",{"class":"skuBestPrice"}).text

	return elektra_name,elektra_price


def parseCoppel(url,browser):
	#descripción
	#tiempo de entrega
	#booleano para el cŕedito
	#tipo de crédito
	browser.get(url)
	html = browser.execute_script("return document.body.innerHTML")

	soup = BeautifulSoup(html,"lxml")
	
	coppel_name = soup.find("h1",{"class":"main_header"}).text
	coppel_price = soup.find("span",{"itemprop":"price"}).text
	
	#Obtención de pagos
	div = soup.find('div', {'class':'p_credito'})
	children = div.findChildren("p" , recursive=False)
	for child in children:
		pagos = child.get_text()
		pagos = pagos.split('\n')
		pagos = pagos[0] + pagos[1].strip()
		pagos = pagos.split('(')[1].split('*')[0].strip()
		coppel_pagos = pagos
	
	
	#Obtención de garantía
	div = soup.find('li', {'class':'beneficio_garantia'})
	children = div.findChildren("span", recursive=False)
	for child in children:
		garantia = child.get_text().split('\n')[2].strip()
		print(garantia)
		coppel_garantia = garantia

	#Obtención de tiempo de entrega
	div = soup.find('div', {'class':'beneficios-product'}).find('ul')
	item = div.findChild()
	coppel_entrega = item.find('span').find('p').text

	return coppel_name, coppel_price, coppel_pagos, coppel_entrega, coppel_garantia
	

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

dic_productos = {}

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
for producto in productos:
	dic_productos[producto] = []
	for empresa in empresas:
		if empresa == "coppel":
			url = get_coppel(producto)
			name,price,payments,delivery,warranty = parseCoppel(url,browser)
			
			total, plazo=payments.split(" en ")
			price = float(re.sub(r'[^\d.]','',price))
			total = float(re.sub(r'[^\d.]','',total))
			plazo = float(re.search(r'\d+',plazo).group(0))
			
			relacion = total/price
			
			deliver1, deliver2 = delivery.split(" a ")
			deliver1 = float(re.search(r'\d+',deliver1).group(0))
			deliver2 = float(re.search(r'\d+',deliver2).group(0))
			
			warranty = float(re.search(r'\d+',warranty).group(0))
			
			dic_productos[producto].append((name.strip(),"coppel",price, total, relacion,plazo,(deliver1,deliver2),warranty))

		
print(dic_productos)


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


