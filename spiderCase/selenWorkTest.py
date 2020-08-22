

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.jd.com")
wait = WebDriverWait(driver,10)

def search():
    try:
        input = wait.until(
            EC.presence_of_element_located((By.ID,"key"))
        )
        btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button"))
        )
        input.send_keys('computer')
        btn.click()
    except TimeoutException:
        #recursoin
        return search()

def next_page(page_number):
    print('getting page %s'%page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input"))
        )
        btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a"))
        )
        input.clear()
        input.send_keys(page_number)
        btn.click()


        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.curr'),str(page_number))
        )
    except TimeoutException:
        return next_page(page_number)
    except StaleElementReferenceException:
        return next_page(page_number)


def main():
    search()
    for i in range(1,20):
        next_page(i)
if __name__ == '__main__':
    main()
    driver.close()
