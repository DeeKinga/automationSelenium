from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


DRIVER_PATH ="E:\QA\it school\chromedriver\\chromedriver.exe"
URL_TO_TEST="https://www.demo.guru99.com/V4/"
USER="mngr503832"
PASSWORD="YzYdevy"

class Login():

    def loginutilizator (self,utilizator,parola):
        print( "Incep testarea")

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe=driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)


        acceptAll = driver.find_element(By.ID,"save")
        acceptAll.click()
        time.sleep(10)

        userId = driver.find_element(By.NAME, "uid")
        userId.send_keys(utilizator)
        time.sleep(10)

        password=driver.find_element(By.NAME,"password")
        password.send_keys(parola)
         
        

        buttonLogin=driver.find_element(By.NAME,"btnLogin")
        buttonLogin.click()
        time.sleep(10)

        test=0
        try:
            actualTitle=driver.title
        except:
            print("test case PASSED")
            test=1

        assert test==1, "Test failed should not login"
        
        driver.close

        time.sleep(10)

    def loginTest(self):
        print( "Incep testarea")

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe=driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)


        acceptAll = driver.find_element(By.ID,"save")
        acceptAll.click()
        time.sleep(10)

        userId = driver.find_element(By.NAME, "uid")
        
        userId.send_keys(USER)

        time.sleep(10)

        password=driver.find_element(By.NAME,"password")
        password.send_keys(PASSWORD)
         
        time.sleep(10)

        buttonLogin=driver.find_element(By.NAME,"btnLogin")
        buttonLogin.click()

        actualTitle=driver.title
        
        
        assert actualTitle=="Guru99 Bank Manager HomePage","test FAILED actual title"


        time.sleep(10)
    

    def loginTestUserNOK(self):
        self.loginutilizator("userNotOK",PASSWORD)
        
    def loginTestPasswordNOK(self):
        self.loginutilizator(USER,"passwordNotok")

    def loginTestUserAndPasswordNOK(self):
        self.loginutilizator("userNotoK","passwordNotok")

    def loginTestEmptyUser(self):
        self.loginutilizator("",PASSWORD)

    def loginTestEmptyPassword(self):
        print( "Incep testarea")

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe=driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)


        acceptAll = driver.find_element(By.ID,"save")
        acceptAll.click()
        time.sleep(10)

        userId = driver.find_element(By.NAME, "uid")
        
        userId.send_keys(USER)

        time.sleep(10)

        password=driver.find_element(By.NAME,"password")
        password.send_keys("")
         
        

        buttonLogin=driver.find_element(By.NAME,"btnLogin")
        buttonLogin.click()


        time.sleep(10)
        
        find= 0
        try:
            driver.find_element(By.ID, "message18")
            find= 1
        except:
            find=0

        assert find==1," Message password empty not found."
        time.sleep(10)


        driver.close

        time.sleep(10)

logintest=Login()

logintest.loginTest()

logintest.loginTestUserNOK()

logintest.loginTestPasswordNOK()

logintest.loginTestUserAndPasswordNOK()

logintest.loginTestEmptyUser()

logintest.loginTestEmptyPassword()

