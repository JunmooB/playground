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

    # 이메일 입력 필드 찾기
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="아이디(이메일)"]')))
    email_field.click()  # 필드를 클릭하여 포커스 설정
    email_field.send_keys(Keys.CONTROL + 'a')  # 모든 텍스트 선택 (Windows/Linux의 경우)
    email_field.send_keys(Keys.BACKSPACE) 
    email_field.send_keys('junmoo.byun@algograp.com')

    # 비밀번호 입력 필드 찾기
    password_field = driver.find_element(By.XPATH, '//input[@placeholder="비밀번호"]')
    password_field.click()  # 필드를 클릭하여 포커스 설정
    password_field.send_keys(Keys.CONTROL + 'a')  # 모든 텍스트 선택 (Windows/Linux의 경우)
    password_field.send_keys(Keys.BACKSPACE) 
    password_field.send_keys('Algograp')


    # 로그인 버튼 찾기
    login_button = driver.find_element(By.XPATH, '//button[text()="로그인"]')
    login_button.click()
    time.sleep(1)  # 1초 대기, 페이지 로딩 상황에 맞게 조정

    
    # numbers = list(range(2002, 2004)) + [2015, 2017] + list(range(2021, 2022)) + \
    #         [2025, 2028, 2032] + list(range(2034, 2064)) + list(range(2065, 2109)) + list(range(2111, 2188)) + \
    #         list(range(2229, 2346)) + list(range(2347, 2562)) + list(range(2563,2763))
    
    
    # numbers = list(range(2240, 2346)) + list(range(2347, 2562)) # 태완 추가  list(range(태완 끝,2562))
    numbers = list(range(1498, 1501))
    for search_element in numbers:
        # url 접속
        search_element = str(search_element)
        driver.get('http://dlh.algograp.com:17300/catalog/')
        
        # 로드 대기
        wait = WebDriverWait(driver, 20)

        #dlh 클릭
        first_element = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@class="MuiTreeItem-label"])[1]')))  
        first_element.click()

        
        time.sleep(2)  # 5초 대기, 페이지 로딩 상황에 맞게 조정
        

        # WebDriverWait을 사용하여 요소가 클릭 가능할 때까지 기다립니다.
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다립니다.
        
        # kmac_test 스키마 클릭
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@class="p-0 m-0 detail_link" and text()="kmac_test"]')))
        element.click()
        time.sleep(0.5)

        # 테이블 목록 열기
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다립니다.

        tables_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "MuiTreeItem-label") and contains(text(), "Tables")]')))

        tables_tab.click()

        time.sleep(1)

        # 테이블 검색 
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inputSearchKeyword')))
        input_element.send_keys(search_element) # 0000_nltk
        time.sleep(0.5)

        # 테이블 검색 버튼 클릭
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.px-3')
        button.click()
        time.sleep(1)

        # 테이블 선택
        xpath_expression = f'//p[@class="p-0 m-0 detail_link" and text()="{search_element}_nltk"]'
        search_table = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
        search_table.click()
        time.sleep(1)

        
        # 데이터 가공 드롭다운 메뉴 토글
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn-dark.btn-sm.dropdown-toggle')
        button.click()
        time.sleep(1)

        # 테이블 데이터 벡터 임베딩 버튼 클릭
        split_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="dropdown-item" and text()="테이블 데이터 벡터 임베딩"]')))
        split_element.click()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading")))
        time.sleep(17)

        # 전체 체크박스 체크
        embedding_model_span  = driver.find_element(By.XPATH, "//span[text()='임베딩 모델']")
        all_click = embedding_model_span.find_element(By.XPATH, "./preceding-sibling::input[@type='checkbox' and @class='form-check-input']")
        all_click.click()
        time.sleep(0.5)

        # 첫 번째 입력 필드가 입력 가능한 상태가 될 때까지 기다림
        input1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="embeddingModelList[0]?.vectorTableName"]'))
        )

        # 현재 값 지우기
        input1.clear()
        
        # 새 값 입력
        input1.send_keys(f"bge_{search_element}_nltk")  # 여기에 새 값을 입력하세요
        time.sleep(0.5)

        # 두 번째 입력 필드를 찾고 입력하기
        input2 = driver.find_element(By.CSS_SELECTOR, 'input[name="embeddingModelList[1]?.vectorTableName"]')
        input2.clear()
        input2.send_keys(f"minilm_{search_element}_nltk")  # 여기에 두 번째 값 입력하세요
        time.sleep(0.5)

        # 세 번째 입력 필드를 찾고 입력하기
        input3 = driver.find_element(By.CSS_SELECTOR, 'input[name="embeddingModelList[2]?.vectorTableName"]')
        input3.clear()
        input3.send_keys(f"krsbert_{search_element}_nltk")  # 여기에 세 번째 값 입력하세요
        time.sleep(0.5)

        # 클릭 방해하는 footer 지우기
        driver.execute_script("document.querySelector('.footer.footer-sticky').style.display = 'none';")
        target_td = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[text()='string']"))
        )
        time.sleep(0.5)

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
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(), '벡터 임베딩 실행')]")))
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
        time.sleep(1)
except:
    error.append(search_element)
    print(error)

finally:
    # 브라우저 종료
    driver.quit()

driver.quit()