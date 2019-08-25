#bit.ly/GShackchallenge
import re
import subprocess

#Crawler mercadolibre
def mercadolibre(busqueda):

    link ='https://listado.mercadolibre.com.mx/'
    busqueda = re.sub(' ','-',busqueda)
    link = link + busqueda
    subprocess.call(["bash", "mercadolibre.sh" , link])

#Crawler coppel
def coppel(busqueda):
    link = "https://www.google.com.mx/search?q=coppel"
    busqueda = re.sub(' ','+',busqueda)
    link = link + busqueda
    subprocess.call(["bash", "coppel.sh" , link])

#Pruebas
mercadolibre('pantalones levis')
coppel('nintendo switch')