from selenium.webdriver.common.by import By

from currentproj.pages.NewOrder import NewData


class TextPage:
    def __init__(self,driver):
        self.driver = driver
    #self.driver.find_element(By.XPATH,"//button[text()='New Order']").click()
    homepage=(By.XPATH,"//button[text()='New Order']")

    def homepages(self):
        self.driver.find_element(*TextPage.homepage).click()
        myorderss = NewData(self.driver)
        return myorderss



