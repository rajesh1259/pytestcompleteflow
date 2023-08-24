import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions

from currentproj.baseclasss import BaseClass
from currentproj.conftest import driver
from currentproj.pages.HomePgae import TextPage
from currentproj.pages.NewOrder import NewData

chrome_options = ChromeOptions()



# Specify the path to the WebDriver service executable
#from lamdapro.lamtest import chrome_options
from selenium.webdriver.chrome.options import Options

#webdriver_service = Service('/Users/vaibhavlutade/PycharmProjects/pytestproject/currentproj/chromedriver599')
#driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the login page
#@pytest.mark.usefixtures("mintex")




class TestExample(BaseClass):
    def test_sinch(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID,"mobile").send_keys("9823521834")
        #time.sleep(5)
        self.driver.find_element(By.ID, "Log In button").click()

        #time.sleep(5)
        self.driver.find_element(By.ID,"Password").send_keys("repos1234")
        self.driver.find_element(By.ID, "Log In button").click()


        time.sleep(5)

    #@pytest.mark.skip
    def test_placeorder(self):
        myhome=TextPage(self.driver)
        myorderss=myhome.homepages()
        time.sleep(5)

        #
        myorderss.orderpage().click()
        time.sleep(5)
        myorderss.citylistpage().click()
        time.sleep(5)
        myorderss.citynamefun().click()
        time.sleep(5)
        myorderss.asstselction().click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("Test DG set")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//h5[text()='Test DG set']").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//div[text()='200Ltr']").click()
        time.sleep(5)

        #time.sleep(5)

        self.driver.find_element(By.XPATH, "//button[text()='View Quotes -->']").click()
        time.sleep(5)

        #time.sleep(5)

        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//h5[text()='mayuri pay ']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Proceed To Payment -->']").click()
        time.sleep(5)
        # order_alert=self.driver.find_element(By.XPATH, "//h4[text()='Order Alert!']")
        # assert order_alert == "Order Alert!"
        # self.driver.find_element(By.XPATH, "//h4[text()='Order Alert!']").click()
        time.sleep(5)
        place_elemet= self.driver.find_element(By.XPATH,"//*[@id='alert-dialog-description']/div[3]/a/h6")
        new_element=place_elemet.text
        place_exp= "See placed order."

        time.sleep(5)
        if new_element == place_exp:
            self.driver.find_element(By.XPATH,"//*[@id='alert-dialog-description']/div[3]/a/h6").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//*[@id='main_con']/div[3]/div/div/div/div[2]/div[1]/div/div/a/div[1]/div[2]/div/div").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//p[text()='Request Cancel >']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//a[text()='Request Cancel']").click()
            time.sleep(5)

            self.driver.find_element(By.ID, "outlined-helperText").send_keys("vever")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH, "//button[text()='New Order']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[text()='Door Step Delivery']").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "select_city").click()
            time.sleep(5)
            myorderss.citynamefun().click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"//button[text()='Change']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//h5[text()='Test DG set']").click()
            time.sleep(5)


            self.driver.find_element(By.XPATH, "//div[text()='200Ltr']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[text()='View Quotes -->']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//h5[text()='mayuri pay ']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[text()='Proceed To Payment -->']").click()




            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
            time.sleep(10)


        else:
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
            time.sleep(10)











        #
        #
        # #my asset page
   # @pytest.mark.skip
    def test_myasset(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Assets']").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//p[text()='postman akshay demo']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH,"//option[text()='Month']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//option[text()='Year']").click()
        #time.sleep(5)
        #self.driver.find_element(By.XPATH, "//button[text()='View ']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Datum Dispenses']").click()
        #time.sleep(5)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='STATEMENT']").click()
        #time.sleep(5)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)




        self.driver.find_element(By.XPATH, "//span[text()='Dispense']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//p[text()='Select Sub Asset']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search By Name']").send_keys("other sub asset")

        self.driver.find_element(By.XPATH, "//img[@alt='asset image']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[text()='200Lt']").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Dispense']").click()
        self.driver.find_element(By.XPATH, "//button[text()='STATEMENT']").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Vectorfilter']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div[2]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='16']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='17']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Send Mail']").click()
        self.driver.find_element(By.XPATH, "//button[text()='SUB-ASSETS']").click()
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Add Sub Asset']").click()
        self.driver.find_element(By.XPATH, "//p[text()='DG set']").click()
        self.driver.find_element(By.NAME, "name").send_keys("KA668844")
        self.driver.find_element(By.NAME, "mobile").send_keys("9090989876")
        self.driver.find_element(By.NAME, "is_telematics").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1uvydh2']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//li[text()='FLEET-X']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Create Sub-Asset']").click()
        time.sleep(5)

    #@pytest.mark.skip
    def test_orders_page(self):
        #my orders page
        self.driver.find_element(By.XPATH,"//span[text()='My Orders']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[3][@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary MuiTab-fullWidth css-96j8ql']").click()
        time.sleep(5)
        elements=self.driver.find_elements(By.XPATH,"//button[text()='Pay Now']")
        time.sleep(5)
        if elements:
            elements[0].click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//button[text()='Pay']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//ul[@class='payment_mode']").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "HDFCCRDC").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "cardNumberField").send_keys("4012001037141112")
        time.sleep(5)
        self.driver.find_element(By.ID, "cardHolderNameField").send_keys("mahesh")
        time.sleep(5)
        self.driver.find_element(By.NAME, "expiryDateField").send_keys("1225")
        time.sleep(5)
        self.driver.find_element(By.NAME, "cvvNumberField").send_keys("125")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='TransactionForm']/div[3]/section/div/div[4]/div[2]/div[5]/div[2]/div[3]/div[1]/a").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(5)

    def test_myprofile(self):
        self.driver.implicitly_wait(15)

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/header/div[1]/a[2]").click()
       # time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div/div/div[2]/div/p[2]/img").click()
        #time.sleep(5)
        self.driver.find_element(By.NAME, "customer_name").clear()
        self.driver.find_element(By.NAME, "customer_name").send_keys("akshay test account staging")
       # time.sleep(5)

        self.driver.find_element(By.NAME, "company_name").clear()
        self.driver.find_element(By.NAME, "company_name").send_keys("Akshay Pvt lTD")
        #time.sleep(5)

        self.driver.find_element(By.NAME, "mobile").clear()
        self.driver.find_element(By.NAME, "mobile").send_keys("9823521834")

        self.driver.find_element(By.NAME, "pan_card").clear()
        self.driver.find_element(By.NAME, "pan_card").send_keys("jugftfgftf")

        self.driver.find_element(By.NAME, "customer_address").clear()
        self.driver.find_element(By.NAME, "customer_address").send_keys("Repos Energy's, Ashok Nagar, Pune, India")

        self.driver.find_element(By.NAME, "pincode").clear()
        self.driver.find_element(By.NAME, "pincode").send_keys("411020")

        self.driver.find_element(By.XPATH, "//button[text()='Edit Details']").click()


    # def test_dashbaoedpage(self):
    #     self.driver.find_element(By.XPATH, "//button[text()='Edit Details']").click()
    #     self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #























































