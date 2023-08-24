from selenium.webdriver.common.by import By

from currentproj.conftest import driver


class NewData:
    def __init__(self,driver):
        self.driver=driver

    #self.driver.find_element(By.XPATH, "//span[text()='Door Step Delivery']").click()
    order1page=(By.XPATH,"//span[text()='Door Step Delivery']")

    #self.driver.find_element(By.ID, "select_city").click()
    citylist=(By.ID,"select_city")

    #self.driver.find_element(By.XPATH, "//li[text()='PUNE']").click()
    cityname=(By.XPATH,"//li[text()='PUNE']")

    selectasset=(By.XPATH,"//p[text()='Select Asset']")




    def orderpage(self):
        return self.driver.find_element(*NewData.order1page)

    def citylistpage(self):
        return self.driver.find_element(*NewData.citylist)

    def citynamefun(self):
        return self.driver.find_element(*NewData.cityname)

    def asstselction(self):
        return self.driver.find_element(*NewData.selectasset)
