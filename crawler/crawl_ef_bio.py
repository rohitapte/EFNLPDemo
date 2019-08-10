from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# if chromedriver is not in your path, you’ll need to add it here
driver = webdriver.Chrome(r'C:\Users\tihor\downloads\chromedriver.exe')

def get_summary_page():
    timeout = 5
    driver.get("https://programme.joinef.com/#/cohort/bdf8fe13-4da6-4efd-9aeb-659c37bd2df7/members")
    try:
        driver.implicitly_wait(15);
        #element_present = EC.text_to_be_present_in_element_value((By.NAME, 'email','yours@example.com'))
        #WebDriverWait(driver, timeout).until(element_present)
        elem = driver.find_element_by_name('email')
        elem.send_keys("rohit@rohitapte.com")
        elem = driver.find_element_by_name('password')
        elem.send_keys("Today123$")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        html=driver.page_source
        #print(html)

    except TimeoutException:
        print("Timed out waiting for page to load")


if __name__ == "__main__":
    get_summary_page()