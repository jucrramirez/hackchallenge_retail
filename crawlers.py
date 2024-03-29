#bit.ly/GShackchallenge
import re
import subprocess
from requests_html import HTMLSession

#Crawler mercadolibre
def mercadolibre(busqueda):

    link ='https://listado.mercadolibre.com.mx/'
    busqueda = re.sub(' ','-',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "mercadolibre.sh" , link])
    return url.decode('utf-8').strip()

#Crawler coppel
def coppel(busqueda):
    link = "https://www.google.com.mx/search?q=coppel"
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "coppel.sh" , link])
    return url.decode('utf-8').strip()

def liverpool(busqueda):
    link = "https://www.google.com.mx/search?q=liverpool"
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "liverpool.sh" , link])
    return url.decode('utf-8').strip()

def amazon(busqueda):
    link = "https://www.amazon.com.mx/s?k="
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    url = subprocess.check_output(["bash", "amazon.sh" , link])
    return url.decode('utf-8').strip()

def walmart(busqueda):
    link = "https://www.walmart.com.mx/productos?Ntt="
    busqueda = re.sub(' ','%20',busqueda)
    link = link + busqueda
    
    session = HTMLSession()
    r = session.get(link)
    r.html.render()
    div = r.html.find('div[data-automation-id="production-index-0"]', first=False)
    for element in div:
        print(element)
    
    
#Pruebas
#url = mercadolibre('pantalones levis')
#coppel('nintendo switch')
#liverpool('nintendo switch')
#amazon('nintendo switch')
walmart('nintendo switch')
