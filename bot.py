from selenium import webdriver
from time import sleep

numero_votos = int(input('Quantoas vezes você quer votar? '))
globo_email = 'fernandinho.nco@gmail.com'  # seu email
globo_pass = '03f18l19f'  # sua senha
base_URL = 'https://login.globo.com/login/6694?url=https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml&tam=WIDGET'

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(base_URL)

driver.find_element_by_id('login').send_keys(globo_email)
driver.find_element_by_id('password').send_keys(globo_pass)
driver.find_element_by_class_name('button').click()
sleep(5)

for c in range(1, numero_votos):
    cont = 1
    participantes = driver.find_elements_by_class_name('_3XS4Y0WYa0gelPf1sxIlOX')
    participantes[1].click()
    sleep(10)
    while cont != 0:

        try:
            driver.find_element_by_css_selector('._2RlpFUvPRVdsXs_oOyQ_pN').click()
            cont = 0
        except:
            # capcha verification
            print('capcha verification')
        sleep(10)

driver.quit()
