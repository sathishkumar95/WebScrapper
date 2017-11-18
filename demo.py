from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def initchrome():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/home/primenumbers/chromedriver", chrome_options=options)
    driver.maximize_window()
    return driver


def getLatestTab(driver):
    new_window_handle = driver.window_handles[-1]
    driver.switch_to.window(new_window_handle)
    return driver


def iterpage(driver):
    links = driver.find_elements_by_css_selector('#result-pane > div > div > div.search_title > a')
    for i in links:
        print (str(i.get_attribute('href')))

    driver = getLatestTab(driver)
    return driver


def feedpagelinks(driver):
    for i in range(1, 5):
        #css = 'ul.pagination > li.active + li > a'
        #css ='#pagination-container > div > ul>li.active+li>a'
        """element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#pagination-container > div > ul>li.active+li')))
        #nextpage = driver.find_element_by_css_selector(css)
        """

        try:

            driver.implicitly_wait(30)
            element = driver.find_element_by_css_selector('#pagination-container > div > ul > li.active+li >a')
            #nextpage.click()
            driver.execute_script("arguments[0].click();", element)
            driver = getLatestTab(driver)
            driver = iterpage(driver)
        except Exception as e:
            print("Element not found or not clicked")
            print e
            driver.close()

    return driver


def login(driver):
    username = driver.find_element_by_id('user_id_form')
    password = driver.find_element_by_id('password_form')
    # username.clear()
    # password.clear()
    username.send_keys("sathishp.railway@gmail.com")
    password.send_keys("pq4u5ql3")

    password.submit()
    sleep(1)
    driver.implicitly_wait(30)


def quitall(driver):
    driver.quit()
    driver.close()


def main():

    driver = initchrome()
    try:
        driver.get("https://www.primetenders.com/search?query=domain:eprocure.gov.in&page=1")
        link = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(6) > a:nth-child(1)')))
        driver.implicitly_wait(30)
        link.click()
    except Exception as e:
        print("Something went wrong")
        print e
        driver.close()

    login(driver)
    driver = iterpage(driver)
    driver = feedpagelinks(driver)
    quitall(driver)

if __name__ == '__main__':
    main()

