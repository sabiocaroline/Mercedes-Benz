# pip install pandas requests beautifulsoup4

import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL da página
url = 'https://esterbernardes22.github.io/Mercedes.benz/index.html'

# Fazer o download da página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas as tabelas na página
tables = soup.find_all('table')

# Iterar sobre as tabelas
for i, table in enumerate(tables):
    
    df = pd.read_html(str(table))[0]

    # Imprimir as informações da tabela
    print(f'Informações da Tabela {i + 1}:\n')
    print(df)
    print('\n' + '-' * 50 + '\n')
