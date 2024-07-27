from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

def button_click(xpath):
    button = driver.find_element('xpath', xpath)
    button.click()
    
def input_text(xpath, text):
    _input = driver.find_element('xpath', xpath)
    _input.send_keys(Keys.CONTROL + 'a')
    _input.send_keys(Keys.BACKSPACE)
    _input.send_keys(text)
    
def wait_button_click(xpath, seconds):
    try:
        login_button = WebDriverWait(driver, seconds).until(
            EC.presence_of_element_located(('xpath', xpath))  # 로그인 버튼 (예: ID가 'loginButton')
        )
        # 로그인 버튼 클릭
        login_button.click()
    except:
        print("버튼을 찾을 수 없습니다.")

def scroll_button(xpath):
    element = driver.find_element('xpath', xpath)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()

# ChromeOptions 객체 생성
options = webdriver.ChromeOptions()

# 브라우저 캐시 비활성화 설정 추가
options.add_argument("--disable-application-cache")
options.add_argument("--disk-cache-size=0")
options.add_argument("--aggressive-cache-discard")
options.add_argument("--disable-cache")


# 파일 넘버 정의
# numbers = list(range(2531, 2763))
# numbers.remove(2562)

# numbers_as_str = [str(i).zfill(4) for i in range(287, 498)]
numbers_as_str = [str(i).zfill(4) for i in range(393, 498)]
eliminate_num = ['0290', '0295', '0297', '0299', '0308', '0321', '0322', '0333', '0334', '0338', '0340', '0341', '0343', '0344',
'0347', '0348', '0349', '0353', '0357', '0359', '0362', '0363', '0364', '0365', '0366', '0367', '0368', '0393', '0441', '0460', '0468' ]

set1 = set(numbers_as_str)
set2 = set(eliminate_num)
numbers = list(set1-set2)
numbers.sort()

error_list = []
for number in numbers:
    try:
        url = "http://sbtglobal2.iptime.org:17300/login/"
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(0.5)

        id_xpath = '//*[@id="__next"]/div/div/div/div/div/div/form/div[1]/input'
        text_id = 'junmoo.byun@algograp.com'
        input_text(id_xpath, text_id)

        password_xpath = '//*[@id="__next"]/div/div/div/div/div/div/form/div[2]/input'
        text_password = 'Algograp'
        input_text(password_xpath, text_password)

        login_xpath = '//*[@id="__next"]/div/div/div/div/div/div/form/div[3]/div[1]/button'
        button_click(login_xpath)
        time.sleep(1)

        # "dlh" click
        dlh_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/p'
        wait_button_click(dlh_xpath, 5)
        time.sleep(1)

        # 'kmac_test' click
        kmac_test_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/p'
        wait_button_click(kmac_test_xpath, 5)
        time.sleep(0.5)

        # '테이블' 클릭
        table_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[2]/ul/li[2]/a'
        wait_button_click(table_xpath, 5)
        time.sleep(0.5)

        # '텍스트' 입력 및 검색
        text_input_xpath = '//*[@id="inputSearchKeyword"]'
        file_name = number
        input_text(text_input_xpath,file_name)
        button_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/button'
        button_click(button_xpath)
        time.sleep(1)
        # 파일 들어가기
        #2506
        # file_click_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/p'
        #2507
        file_click_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/p'
        wait_button_click(file_click_xpath, 10)
        # 잠시 대기
        time.sleep(1)

        data_procss_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div/button'
        button_click(data_procss_xpath)

        seg_xpath ='//*[@id="__next"]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div/ul/li[3]/a'
        button_click(seg_xpath)

        # 잠시 대기
        time.sleep(15)

        # nltk 클릭
        nltk_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/form/div[1]/div/table/tbody/tr[2]/td[1]/input'
        # button_click(nltk_xpath)
        button_click(nltk_xpath)
        time.sleep(0.5)

        # 스크롤 아래로 내리기
        sel_col_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/form/div[2]/div[1]/table/tbody/tr[3]/td[1]/input'
        button = driver.find_element('xpath', sel_col_xpath)
        button.send_keys(Keys.PAGE_DOWN)
        button.send_keys(Keys.PAGE_DOWN)
        button.send_keys(Keys.PAGE_DOWN)
        button.send_keys(Keys.PAGE_DOWN)
        button.click()
        time.sleep(0.5)

        execute_xpath = '//*[@id="__next"]/div[3]/div[3]/div/div/form/div[4]/div/button'
        button_click(execute_xpath)

        time.sleep(0.5)
        last_xpath = '/html/body/div[2]/div/div/div[2]/button[2]'        
        button = driver.find_element('xpath', last_xpath)
        button.click()
        
        # 잠시 대기
        time.sleep(5)

        # 브라우저 닫기
        driver.quit()
        
        time.sleep(1)
    except:
        print("실패한 파일 :", number)
        error_list.append(number)


print(error_list)