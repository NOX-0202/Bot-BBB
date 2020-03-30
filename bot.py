from selenium import webdriver
from time import sleep

globo_email = '' #seu email
globo_pass = '' # sua senha
base_URL = 'https://login.globo.com/login/6694?url=https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml&tam=WIDGET'

# CONECTANDO AO SITE
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(base_URL)

# FAZENDO O LOGIN
driver.find_element_by_id('login').send_keys(globo_email)
driver.find_element_by_id('password').send_keys(globo_pass)
driver.find_element_by_class_name('button').click()
sleep(3)

for c in range(1, 10):
    # VOTANDO
    sleep(5)
    participantes = driver.find_elements_by_class_name('_18p_tzl-nqcb9ABOQXokP0')
    participantes[1].click()
    # aqui ele vai esperar 5 sec pra tu clicar no caralho da imagem
    sleep(7)
    # agora ele vai clicar em votar novamente
    driver.find_element_by_class_name('_3HO0UFrn-QxI5rQexA1hj3').click()

