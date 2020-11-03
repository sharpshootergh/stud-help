from selenium import webdriver
from time import sleep
from inputs import pw
from inputs import un


class WebBot:
    def __init__(self,un,pw):
        self.driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
#goto university protal
        self.driver.get('https://portal.ucc.edu.gh/')
        sleep(3)
#find user name input box 
        self.driver.find_element_by_xpath('/html/body/main/div[2]/section[2]/form/div[1]/div/input')\
            .send_keys(un)
#find user passwd input box
        self.driver.find_element_by_xpath('/html/body/main/div[2]/section[2]/form/div[2]/div/input')\
            .send_keys(pw)
#find send button 
        self.driver.find_element_by_xpath('/html/body/main/div[2]/section[2]/form/div[3]/div[1]/input')\
            .click()
        sleep(2)
#nav site 
        self.driver.switch_to.frame("content")\

        self.driver.find_element_by_xpath('/html/body/div/div/div[7]/div/div/section/a')\
            .click()
        sleep(2)

        
#get email 
        email=self.driver.find_element_by_class_name("text-danger")
        print("your email address is:" + email.text)
#get password 
        passwd=self.driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div/section/h6[2]/span")
        print("your password is:" + passwd.text)


WebBot(un, pw)
