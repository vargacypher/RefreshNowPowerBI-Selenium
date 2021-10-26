# -*- coding: utf-8 -*-
__author__ = 'Guilherme Cardoso de Vargas'
__version__ = 1.0
__maintainer__ = 'Guilherme Cardoso de Vargas'
__email__ = 'vargas93626@gmail.com'
__status__ = 'Development'


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


def main():
    '''LINK PARA LOGIN NO POWER BI'''
    powerbi = 'https://app.powerbi.com/home?redirectedFromSignup=1&noSignUpCheck=1&response=AlreadyAssignedLicense'

    '''CONFIGURAÇÕES CHROME DRIVE'''
    
    option = webdriver.ChromeOptions()
    #(NO browser window)
    #option.headless = True
    #option.incognito = True

    #BROWSER OBJECT / NAVIGATE TO POWER BI / MAXIMIZE WINDOW 
    browser = webdriver.Chrome(executable_path='chromedriver.exe' , options=option)
    browser.get(powerbi)
    action = ActionChains(browser)
    browser.maximize_window()

    #INSERE O EMAIL E CLICA EM NEXT
    time.sleep(4)
    bi_email = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i0116'))) 
    bi_email.send_keys('EMAIL')
    bi_email.send_keys(Keys.ENTER)

    #INSERE A SENHA E CLICA EM ENTRAR
    time.sleep(4)
    bi_pass = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i0118')))
    bi_pass.send_keys('PASSWORD')
    bi_pass.send_keys(Keys.ENTER)

# Clica para nao se manter conectado
    time.sleep(4)
    yes_choice = browser.find_element_by_id('idSIButton9')
    yes_choice.send_keys(Keys.SHIFT, Keys.TAB, Keys.ENTER)

    #LOCALIZA A WORKSPACE 
    time.sleep(4)
    browser.get('https://app.powerbi.com/groups/72074a89-eb8-80f9-1c94fb7c1c4e/list')

    #Vai até a DIV para localizar o botão de att
    time.sleep(5)
    div_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-virtual-scroll-content-wrapper']"))
    )

    #Localização da base a ser atualizada através do elemento com seu index
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[1] #index

    
    #Mimetiza mouse
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Atualizar agora']"))
    )
    
    buttonatualizarpainel_elem.click()
    
    print ('Dataset Atualizado')

#FECHAR O BROWSER
    time.sleep(8)
    browser.close()
    browser.quit()

if __name__ == '__main__':
    main()
