from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



@given('open prowser')
def driver(context):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        context.driver = webdriver.Chrome(options=chrome_options)
        context.driver.maximize_window()
        context.driver.get('wrong one ')
        print("first option started")
    except Exception as e:
        print("second option started")
        context.driver.get("https://www.google.com/")
    time.sleep(2)


    

@when('open google "{search_trem}"')
def google(context, search_trem):
    try:
        search_input = WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']"))
        )
        search_input.send_keys(search_trem)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(e)
        time.sleep(2)
        




@when('open the page')
def search(context):
    try:
        find_page = WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div"))
        )
        find_page.click()
        time.sleep(2)
    except Exception as e:
        print(f"error {e}")
        aaa =  WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span"))
        )
        aaa.click()
        time.sleep(2)




@then('wait and close')
def last(context):
    try:
        print("perfect job")  

    except Exception as e:
        print("something went wrong:", e)


        

@then('last')
def last(context):
        try:
            context.driver.get("https://www.google.com/")
            search = WebDriverWait(context.driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='APjFqb']"))
            )
            search.send_keys("selenium")
            search.send_keys(Keys.RETURN)
            time.sleep(2)
            aaa =  WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3/span")))
            aaa.click()
            time.sleep(2)
            
        except Exception as e:
            print(f"error{e}")
            search.send_keys("selenium")
            search.send_keys(Keys.RETURN)
            context.driver.get("https://www.google.com/")
            search = WebDriverWait(context.driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='APjFqb']")))
            time.sleep(2)
            aaa =  WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")))
            aaa.click()
            time.sleep(2)
        
        



@then('last2')
def last2(context):
        try:
            context.driver.get("https://www.google.com/")
            search = WebDriverWait(context.driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='APjFqb']"))
            )
            search.send_keys("hello")
            search.send_keys(Keys.RETURN)
            time.sleep(2)
            aaa =  WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3/span")))
            aaa.click()
            time.sleep(2)
        except Exception:
            aaa = WebDriverWait(context.driver,50).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3"))
            )
        except Exception as e:

            search.send_keys("gello")
            search.send_keys(Keys.RETURN)
            context.driver.get("https://www.google.com/")
            search = WebDriverWait(context.driver,40).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='APjFqb']")))
            time.sleep(2)
            aaa =  WebDriverWait(context.driver,60).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[4]/div/div/div[1]/div/div/span/a/h3/span")))
            aaa.click()
            time.sleep(2)
        except Exception as e:
            aaa = WebDriverWait(context.driver,50).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='rso']/div[4]/div/div/div[1]/div/div/span/a/h3/span"))
            )
        finally:
            time.sleep(2)
            context.driver.quit()



@then('quit')
def quit(context):
    context.driver.quit()


