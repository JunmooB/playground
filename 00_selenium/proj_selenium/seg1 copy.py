from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Chrome 웹 드라이버 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 UI를 띄우지 않고 실행하려면 주석 해제
# driver_path = 'C:/Users/chanhoe.Hur/Downloads/automate/automate/chromedriver.exe'  # 크롬 드라이버 경로 설정
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://codeit.kr')

# service = Service(driver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)

error =[]
try:
    # 웹 페이지 열기
    driver.get('http://dlh.algograp.com:17300/catalog/')
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="아이디(이메일)"]')))
    # email_field = driver.find_element(By.XPATH, '//input[@placeholder="아이디(이메일)"]')
    email_field.click()  # 필드를 클릭하여 포커스 설정
    email_field.send_keys(Keys.CONTROL + 'a')  # 모든 텍스트 선택 (Windows/Linux의 경우)
    email_field.send_keys(Keys.BACKSPACE) 
    email_field.send_keys('junmoo.byun@algograp.com')
    time.sleep(0.5)  # 5초 대기, 페이지 로딩 상황에 맞게 조정

    # 이메일 입력 필드 찾기
    # email_field = driver.find_element(By.ID, 'email')  # 이메일 입력 필드의 ID를 사용 (혹은 다른 선택자 사용)
    password_field = driver.find_element(By.XPATH, '//input[@placeholder="비밀번호"]')
    password_field.click()  # 필드를 클릭하여 포커스 설정
    password_field.send_keys(Keys.CONTROL + 'a')  # 모든 텍스트 선택 (Windows/Linux의 경우)
    password_field.send_keys(Keys.BACKSPACE) 
    password_field.send_keys('Algograp')
    time.sleep(0.5)
    # time.sleep(5)  # 5초 대기, 페이지 로딩 상황에 맞게 조정

    # 비밀번호 입력 필드 찾기
    # password_field = driver.find_element(By.ID, 'password')  # 비밀번호 입력 필드의 ID를 사용 (혹은 다른 선택자 사용)

    # 로그인 버튼 찾기
    # login_button = driver.find_element(By.ID, 'login-button')  # 로그인 버튼의 ID를 사용 (혹은 다른 선택자 사용)
    login_button = driver.find_element(By.XPATH, '//button[text()="로그인"]')
    login_button.click()
    time.sleep(1)  # 1초 대기, 페이지 로딩 상황에 맞게 조정

    # remove_list_number = [1577, 1580, 1592, 1600, 1603, 1607, 1627, 1636, 1644, 1646, 1647, 1648, 1651, 1652, 1656, 1667, 1683, 1691, 1699, 1705, 1715, 1716,1726,1734,1735,1736,1747,1755,1756,1782,1783,1786,1788,1789,1790,1793,1794,1798,1799,1804,1807,1821,1824,1829,1832,1839,1840,1841,1842,1847,1848,1850,1852,1853,1857,1858,1862,1863,1866,1875,1877,1880,1881,1886,1887,1889,1892,1894,1896,1899,1900,1905,1909,1910]
    # remove_list = [num_str for num_str in remove_list_number]
    # search_list = [str(number) for number in range(1509, 1914) if number not in remove_list]

    # search_list = ['2526', '2536', '2544', '2553', '2563', '2578', '2583', '2596', '2606', '2630', '2661', '2662',
    #                 '2671', '2672', '2673', '2684', '2689', '2690', '2701', '2702', '2707', '2709', '2729', '2746']

    # temps = [2064, 2109, 2110] + list(range(2188, 2229)) + [2346]
    # image_file_list = []
    # for temp in temps:
    #     image_file_list.append(str(temp)) 
    # res_temps = [str(num) for num in range(2301, 2401)]

    # numbers = []
    # for res_temp in res_temps:
    #     if res_temp not in image_file_list:
    #         numbers.append(res_temp)
    # numbers = ['0294', '0312', '0318', '0319', '0360', '0361', '0369', '0371' '0372', '0373', '0374', '0375', '0376', '0378', '0380', '0384', '0386', '0388']

    # 998~1500까지 정의
    # numbers = [list(range(998, 1026)) + list(range(1027, 1036)) + list(range(1037, 1049)) + list(range(1050, 1052)) + \
    #            list(range(1053, 1057)) + list(range(1058, 1110)) + list(range(1111, 1146)) + list(range(1147, 1153)) + \
    #             list(range(1154, 1162)) + [1163, 1165, 1166] + list(range(1169, 1174)) + list(range(1175, 1295))]

    numbers = list(range(1273, 1283))
    for search_element in numbers:
        search_element = str(search_element)
        driver.get('http://dlh.algograp.com:17300/catalog/')
        # image 데이터가 아닌 경우
    
        wait = WebDriverWait(driver, 20)
        first_element = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@class="MuiTreeItem-label"])[1]')))  
        # first_element = driver.find_element(By.XPATH, '(//div[@class="MuiTreeItem-label"])[1]')
        first_element.click()
        # 로그인 후 페이지가 로딩되기를 기다리기 (필요시)
        time.sleep(2)  # 5초 대기, 페이지 로딩 상황에 맞게 조정

        # WebDriverWait을 사용하여 요소가 클릭 가능할 때까지 기다립니다.
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다립니다.
        
        # 주어진 XPath로 요소를 찾습니다.
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@class="p-0 m-0 detail_link" and text()="kmac_test"]')))
        
        # 요소를 클릭합니다.
        element.click()
        time.sleep(0.5)
        # time.sleep(1)  # 5초 대기, 페이지 로딩 상황에 맞게 조정

        # <p> 요소 찾기 및 클릭 (XPath 사용)
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다립니다.

        tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "MuiTreeItem-label") and contains(text(), "Tables")]')))

        tables_tab.click()

        time.sleep(1)  
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inputSearchKeyword')))
        
        # 입력값 설정
        input_element.send_keys(search_element)

        # # 버튼 찾기 및 클릭 (CSS 선택자 사용)
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.px-3')
        button.click()
        time.sleep(1)

        # 테이블 선택
        xpath_expression = f'//p[@class="p-0 m-0 detail_link" and text()="{search_element}"]'
        search_table = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
        search_table.click()
        time.sleep(1)

        # # 버튼 찾기 및 클릭 (XPath 사용)
        # button = driver.find_element(By.XPATH, '//button[@class="btn btn-dark btn-sm dropdown-toggle"')
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn-dark.btn-sm.dropdown-toggle')
        button.click()
        time.sleep(1)

        # 문단 나누기 버튼 클릭
        split_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="dropdown-item" and text()="테이블 데이터 문단 나누기"]')))
        split_element.click()
        # time.sleep(10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading")))
        # nltk 선택
        # nltk_click = driver.find_element(By.CSS_SELECTOR, 'input.form-check-input and text()=nltk')
        time.sleep(2)
        nltk_span  = driver.find_element(By.XPATH, "//span[text()='nltk']")
        # time.sleep(5)
        nltk_click = nltk_span.find_element(By.XPATH, "./preceding-sibling::input[@type='checkbox' and @class='form-check-input']")
        # nltk_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="form-check-input" and text()="nltk"]')))
        nltk_click.click()
        time.sleep(0.5)

        driver.execute_script("document.querySelector('.footer.footer-sticky').style.display = 'none';")
        target_td = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[text()='string']"))
        )

        # 해당 <td> 요소의 부모 <tr> 요소 찾기
        parent_tr = target_td.find_element(By.XPATH, "./parent::tr")

        # 클릭을 방해할 수 있는 요소가 사라질 때까지 대기
        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://www.algograp.com/"]'))
        )
        # <tr> 요소 내에서 라디오 버튼(input[type='radio']) 찾기
        radio_button = parent_tr.find_element(By.CSS_SELECTOR, "input[type='radio'].form-check-input")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)
        # 라디오 버튼 클릭
        time.sleep(0.5)
        radio_button.click()
        
        # time.sleep(10)



        wait = WebDriverWait(driver, 30)  # 최대 30초까지 기다립니다.
        
        # # '확인' 버튼이 클릭 가능해질 때까지 기다립니다.
        # button = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(), '문단 나누기 실행')]")))
        # print(button)
        # driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(), '문단 나누기 실행')]")))
        driver.execute_script("arguments[0].click();", button)
        # # 버튼을 클릭합니다.
        # button.click()

        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='확인']")))
        
        # # 버튼을 클릭합니다.
        button.click()
        time.sleep(1)
        # button2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='확인']")))
        button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='확인']")))
        
        # # 버튼을 클릭합니다.
        driver.execute_script("arguments[0].click();", button2)
        # time.sleep(5)
except:
    error.append(search_element)
    print(error)

finally:
    # 브라우저 종료
    driver.quit()

driver.quit()