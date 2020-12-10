from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException
import time


CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe" #path to chrome webdriver
SIMILAR_ACCOUNT = "atptour" #account who you want to follow followers of 
USERNAME = "example@email.com" #instagram email
PASSWORD = "password" # instagram password

url = "https://www.instagram.com/"


class InstaFollower:


    def __init__(self):

        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    
    def get_followers(self):
        # method that will call login, find followers, and follow to try and get followers for you
        self.login()
        self.find_followers()
        self.follow()


    def login(self):

        self.driver.get(url)
        time.sleep(2)

        login_input = self.driver.find_element_by_name("username")

        login_input.send_keys(USERNAME)


        password_input = self.driver.find_element_by_name("password")

        password_input.send_keys(PASSWORD)

        button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

        button.click()

        time.sleep(15)








    def find_followers(self):



        input_form = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')

        input_form.send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)


        result = self.driver.find_element_by_css_selector('div.fuqBx a')

        try:
            result.click()
        except ElementClickInterceptedException:
            button = self.driver.find_element_by_css_selector("div.mt3GC button.aOOlW.HoLwm")
            button.click()
            time.sleep(15)
            result.click()


        time.sleep(5)

        followers_link = self.driver.find_element_by_css_selector('a.-nal3')

        followers_link.click()
        
        time.sleep(2)
        scroll = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")


        follow_buttons = [] 

        
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll)
            time.sleep(2)






    def follow(self):

        buttons = self.driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")


        for button in buttons:
        
            try:
                button.click()
            except ElementClickInterceptedException:
                element = self.driver.find_element_by_css_selector("button.aOOlW.HoLwm")
                element.click()
            finally:
                time.sleep(2)











instagram = InstaFollower()

instagram.get_followers()







