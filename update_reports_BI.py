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
from datetime import datetime


def main():
    '''LINK PARA LOGIN NO POWER BI'''
    powerbi = 'https://app.powerbi.com/home?redirectedFromSignup=1&noSignUpCheck=1&response=AlreadyAssignedLicense'

    '''CONFIGURAÇÕES CHROME DRIVE'''
    
    option = webdriver.ChromeOptions()
    #(NO browser window)
    #option.headless = True
    option.incognito = True

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
    bi_pass.send_keys('PASSWD')
    bi_pass.send_keys(Keys.ENTER)

# Clica para nao se manter conectado
    time.sleep(4)
    yes_choice = browser.find_element_by_id('idSIButton9')
    yes_choice.send_keys(Keys.SHIFT, Keys.TAB, Keys.ENTER)

    #LOCALIZA A WORKSPACE 
    time.sleep(4)
    browser.get('https://app.powerbi.com/groups/887074a89-eb16-4e08-80f9-1cFYTc1c4e/list')

    #Vai até a DIV para localizar o botão de att
    time.sleep(5)
    div_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-virtual-scroll-content-wrapper']"))
    )

    #######PRIMEIRO REPORT###########
     #Localização da base a ser atualizada através do elemento com seu index
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[1] #index

    
    #Vai ate o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[2]/div[2]/span/button[1]"))
    )                                             
    buttonatualizarpainel_elem.click()
    time.sleep(2)

    ######SEGUNDO REPORT ########
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[3] #index

    
    #Vai ate o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[4]/div[2]/span/button[1]"))
    )                                             
    buttonatualizarpainel_elem.click()
    time.sleep(2)

    #######TERCEIRO REPORT###########
    #Localização da base a ser atualizada através do elemento com seu index
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[5] #index

    #Vai té o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[6]/div[2]/span/button[1]"))
    )                                             
    
    buttonatualizarpainel_elem.click()
    time.sleep(2)

    #######QUARTO REPORT###########
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[7] #index

    #Vai té o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[8]/div[2]/span/button[1]"))
    )                                             
    
    buttonatualizarpainel_elem.click()
    time.sleep(2)
    
    #######QUINTO REPORT###########
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[9] #index

    #Vai té o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[10]/div[2]/span/button[1]"))
    )                                             
    
    buttonatualizarpainel_elem.click()
    time.sleep(2)
        
    #######SEXTO REPORT###########
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[11] #index

    #Vai té o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[12]/div[2]/span/button[1]"))
    )     

    buttonatualizarpainel_elem.click()
    time.sleep(2)
            
    #######SETIMO REPORT###########
    att_button = browser.find_elements_by_css_selector(".row.ng-star-inserted")[13] #index

    #Vai té o elemento CSS
    action.move_to_element(att_button)

    action.perform()
    
    print("deu bom")
    
    time.sleep(3)
    buttonatualizarpainel_elem = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div/workspace-view/fluent-workspace/mat-sidenav-container/mat-sidenav-content/fluent-workspace-list/fluent-list-table-base/div/cdk-virtual-scroll-viewport/div[1]/div[14]/div[2]/span/button[1]"))
    )   

    buttonatualizarpainel_elem.click()
    time.sleep(2)

    print (f'Datasets Atualizados em : {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')

#FECHAR O BROWSER
    time.sleep(8)
    browser.close()
    browser.quit()


if __name__ == '__main__':
    main()
