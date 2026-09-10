
# Requests sirve para enviar solicitudes HTTP a servidores web, permite interactuar con páginas web.
import requests

# BeautifulSoup sirve para analizar y extraer datos de documentos HTML y XML.
from bs4 import BeautifulSoup

import pandas as pd
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.nike.com/mx/w/mujeres-calzado-5e1x6zy7ok"
response = requests.get(url)
response.encoding = 'utf-8'

texto = BeautifulSoup(response.text, "html.parser")



libros = texto.find_all("div", class_="product-card__info disable-animations")

datos_zapatos = []

for zapato in libros:
    nombre_modelo = zapato.find('div', class_='product-card__title').text.strip() if zapato.find('div', class_='product-card__title') else 'N/A'
    tipo_zapato = zapato.find('div', class_='product-card__subtitle').text.strip() if zapato.find('div', class_='product-card__subtitle') else 'N/A'
    precio_texto = zapato.find('div', class_='product-price').text.strip() if zapato.find('div', class_='product-price') else 'N/A'

    datos_zapatos.append({
        'Nombre del Modelo': nombre_modelo,
        'Tipo de Zapato': tipo_zapato,
        'Precio': precio_texto
    })

df_zapatos = pd.DataFrame(datos_zapatos)
print(df_zapatos)
display(df_zapatos)

"""

with open("texto.py", "w", encoding="utf-8") as f:
    f.write(script_code)
