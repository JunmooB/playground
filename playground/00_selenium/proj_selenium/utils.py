from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
import os
import dotenv

dotenv.load_dotenv()
sever_url = os.getenv('SERVER_URL')
id_email = os.getenv('ID_EMAIL')
password_email = os.getenv('PASSWORD_EMAIL')
def test():
    print("되네")

class MacroProgramDLH():
    def __init__(self, options=[]):
        self.server_url = sever_url
        self.id_email = id_email
        self.password_email = password_email
                
        chrome_options = Options()
        
        # add options
        if options:
            for option in options:
                chrome_options.add_argument(option)
                
        self.driver = webdriver.Chrome(options=chrome_options)
        
        
    def open_page(self):
        self.driver.get(self.server_url)
        time.sleep(0.5)
        
    def login_to_dlh(self,wait_time=10):
        wait =WebDriverWait(self.driver, wait_time)
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="아이디(이메일)"]')))
        email_field.click()  # 필드를 클릭하여 포커스 설정
        email_field.send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        email_field.send_keys(self.id_email)
        
        password_field = self.driver.find_element(By.XPATH, '//input[@placeholder="비밀번호"]')
        password_field.click()  # 필드를 클릭하여 포커스 설정
        password_field.send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        password_field.send_keys(self.password_email)
        
        login_button = self.driver.find_element(By.XPATH, '//button[text()="로그인"]')
        login_button.click()
        time.sleep(0.5)
        
        
           
    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    options = ['--headless']
    options = []
        
    bot = MacroProgramDLH(options)
    bot.open_page()
    bot.login_to_dlh()
    bot.close_browser()
    
    
    
