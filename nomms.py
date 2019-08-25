from requests_html import HTMLSession


session = HTMLSession()
r = session.get("https://www.walmart.com.mx/celulares/smartphones/celulares-desbloqueados/iphone-6s-apple-64-gb-space-gray-reacondicionado-desbloqueado_00071566070284")
r.html.render()
table = r.html.find('h1[itemprop="name"]', first=False)
for tabla in table:
	walmart_name = tabla.text
table = r.html.find('h4[itemprop="price"]', first=False)
for tabla in table:
	walmart_price = tabla.text		

#print(walmart_name)
print(walmart_price)
