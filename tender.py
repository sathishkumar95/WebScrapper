from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

falselinks=[]
dict={}


def login(driver):
    username = driver.find_element_by_id('user_id_form')
    password = driver.find_element_by_id('password_form')
    username.send_keys("sathishp.railway@gmail.com")
    password.send_keys("pq4u5ql3")
    password.submit()
    sleep(1)
    driver.implicitly_wait(30)


def getnumbers(string):
    var = re.findall(r'\d+',string)
    return int(var[0])


def checkvalidity(driver):
    try:
        getLatestTab(driver)
        try:
            element = driver.find_element_by_css_selector('.header_font')
            element = element.text
            if element:
                #print element
                return True
        except Exception as e:
            try:
                element = driver.find_element_by_css_selector('.page_header')
                element = element.text
                if element:
                    #print element
                    return True
            except Exception as e:
                print("Something wrong in css selector")
                print(e)
                return False
            print("Something wrong in css selector")
            print(e)
            return False
    except Exception as e:
        print("Something wrong in css selector")
        print(e)
        return False
    return False


def open_new_tab(driver, url):
    driver.execute_script("window.open('%s', '_blank');" % url)
    sleep(3)
    getLatestTab(driver)


def getLatestTab(driver):
    new_window_handle = driver.window_handles[-1]
    driver.switch_to.window(new_window_handle)
    return driver


def closetab(driver):
    driver.close()
    new_window_handle = driver.window_handles[-1]
    driver.switch_to.window(new_window_handle)
    return  driver


def scanpage(driver):
    driver.switch_to_active_element
    #actions = ActionChains(driver)
    links=[]
    links = driver.find_elements_by_css_selector('#result-pane > div > div > div.search_title > a')
    for i in links:
        var = str(i.get_attribute('href'))
        print var
        code = getnumbers(i.get_attribute('href'))
        dict[code]=0
        open_new_tab(driver, var)
        # driver.switch_to.active_element
        try:
            driver = getLatestTab(driver)
            temp = driver.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
            element = WebDriverWait(driver, 30).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.button_link > a:nth-child(1)'), 'Original Link'))
            element = driver.find_element_by_css_selector('.button_link > a:nth-child(1)')
            element = element.get_attribute('href')
            link = str(element)
            open_new_tab(driver, link)
            driver = getLatestTab(driver)
            # check the validity of link
            if checkvalidity(driver):

                dict[code] = 1
                closetab(driver)
                closetab(driver)

            else:

                dict[code] = -1
                driver = closetab(driver)
                driver = closetab(driver)

        except Exception as e:
            print e
            driver.close()
            driver.quit()

    print dict
    return driver


def initChrome():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/home/primenumbers/chromedriver", chrome_options=options)
    driver.maximize_window()
    return driver

def feedpagelinks(driver):
    driver.switch_to_active_element()
    for i in range(1,5):
        css = 'ul.pagination > li.active + li > a'
        nextpage = driver.find_element_by_css_selector(css)
        nextpage.click()
        url = driver.current_url
        driver.get(url)
        driver = scanpage(driver)


def quitall(driver):
    driver.quit()



driver = initChrome()
try:
    driver.get("https://www.primetenders.com/search?query=domain:eprocure.gov.in&page=1")
    link = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(6) > a:nth-child(1)')))
    driver.implicitly_wait(30)
    link.click()
except Exception as e:
    print("Something went wrong")
    print e
    driver.quit()


login(driver)
driver = scanpage(driver)
driver.switch_to_active_element()
feedpagelinks(driver)
for key,value in dict.iteritems():
    if dict[key]==-1:
        falselinks.append(key)
print falselinks
quitall(driver)



