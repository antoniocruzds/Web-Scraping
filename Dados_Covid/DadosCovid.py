from selenium import webdriver
from time import sleep

#definindo o local do webdriver no computador
driver = webdriver.Chrome(executable_path=r"C:\Users\anton\OneDrive\Área de Trabalho\Curso-de-Selenium\venv\chromedriver.exe")

#definindo o site(url) que queremos entrar
url = "https://covid.saude.gov.br/"
#entrando na url
driver.get(url)
sleep(3)

#encontrando o local do download
dados = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button/font')
#clicando para fazer o download
dados.click()

#fechando o webdriver
driver.quit()