from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configurar o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Acessar o site
navegador.get('https://esterbernardes22.github.io/Mercedes.benz/index.html')
navegador.implicitly_wait(3)

# Encontrar e exibir conteúdo por ID
elemento_por_id = navegador.find_element(By.ID, 'pecas').text
print("Conteúdo por ID:")
print(elemento_por_id)

# Encontrar e exibir conteúdo por TAG_NAME
elementos_por_tags = navegador.find_elements(By.TAG_NAME, 'h1')
print("\nConteúdo por TAG_NAME:")
for elemento in elementos_por_tags:
    print(elemento.text)

# Encontrar e exibir conteúdo por CLASS_NAME
elementos_por_class = navegador.find_elements(By.CLASS_NAME, 'A')
print("\nConteúdo por CLASS_NAME:")
for elemento in elementos_por_class:
    print(elemento.text)

# Encontrar e exibir conteúdo por LINK_TEXT
elemento_por_link_text = navegador.find_element(By.PARTIAL_LINK_TEXT, 'Mercedes Benz')
print("\nConteúdo por LINK_TEXT:")
print(elemento_por_link_text.text)

# Encontrar e exibir conteúdo por CSS_SELECTOR
elemento_por_css_selector = navegador.find_element(By.CSS_SELECTOR, '.card')
print("\nConteúdo por CSS_SELECTOR:")
print(elemento_por_css_selector.text)

# Encontrar e exibir conteúdo por NAME
elemento_por_name = navegador.find_element(By.NAME, 'continue')
print("\nConteúdo por NAME:")
print(elemento_por_name.text)

# Encontrar e exibir conteúdo por XPATH
elemento_por_xpath = navegador.find_element(By.XPATH, '/html/body/header/div/button[1]')
print("\nConteúdo por XPATH:")
print(elemento_por_xpath.text)

# Fechar o navegador
navegador.quit()
