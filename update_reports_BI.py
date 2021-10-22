from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def main():
    '''LINK PARA LOGIN NO POWER BI'''
    powerbi = 'https://app.powerbi.com/home?redirectedFromSignup=1&noSignUpCheck=1&response=AlreadyAssignedLicense'

    '''CONFIGURAÇÕES CHROME DRIVE'''

    #(NO browser window)
    option = webdriver.ChromeOptions()
    #option.headless = True
    #option.incognito = True

    #BROWSER OBJECT / NAVIGATE TO POWER BI / MAXIMIZE WINDOW 
    browser = webdriver.Chrome(executable_path='C:\\Users\\vargas.guilherme\\Desktop\\ScriptsPy\\update_reports_BI\\chromedriver' , options=option)
    browser.get(powerbi)
    browser.maximize_window()

    #INSERE O EMAIL E CLICA EM NEXT
    time.sleep(4)
    bi_email = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i0116'))) 
    bi_email.send_keys('your email')
    bi_email.send_keys(Keys.ENTER)

    #INSERE A SENHA E CLICA EM ENTRAR
    time.sleep(4)
    bi_pass = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i0118')))
    bi_pass.send_keys('your password')
    bi_pass.send_keys(Keys.ENTER)

    '''THIS IS THE PROMPT THAT ASKS IF YOU WANT TO REMAIN LOGGED IN'''
    '''WAIT / STAY ON CURRENT SELECTION / MOVE AND CLICK ON ADJACENT SELECTION'''
    time.sleep(4)
    yes_choice = browser.find_element_by_id('idSIButton9')
    yes_choice.send_keys(Keys.SHIFT, Keys.TAB, Keys.ENTER)

    #LOCALIZA A WORKSPACE E CLICA NELA
    time.sleep(4)
    browser.get('https://app.powerbi.com/groups/72074a89-eb16-4e08-80f9-1c94fb7c1c4e/reports/c170d176-604a-4c9a-b4d3-fa3914eb0a16/ReportSection7797ffc916e2b27c645e')

    #Atualiza o report
    time.sleep(10)
    refresh = browser.find_element_by_id('reportAppBarRefreshBtn').click()
    
    print ('Dataset Atualizado')

#FECHAR O BROWSER
    time.sleep(8)
    browser.close()
    browser.quit()

main()
