from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        
class ContactsPage(BasePage):
    def header_contacts(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu")

    def icon_header_contacts_more_offices(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__arrow-icon")

    def banner(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__logo-tensor")

    def banner_strength_people(self):
        return self.browser.find_element(By.XPATH, "//*[text()='Сила в людях']")

    def more_details_strength_people(self):
        return self.browser.find_element(By.XPATH, "//div[p/text()='Сила в людях']//a[text()='Подробнее']")

    def photo_chronology(self):
        return self.browser.find_elements(By.CSS_SELECTOR, ".s-Grid-container .tensor_ru-About__block3-image-wrapper")
         
    def region(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text")

    def region_list(self,city_name):
        return self.browser.find_elements(By.XPATH, f"//div[@item-parent-key = //div[.='{city_name}']/ancestor::div[@data-qa='item']/@item-key]")
    
    def change_region(self, region):
        return self.browser.find_element(By.CSS_SELECTOR, f".sbis_ru-Region-Panel__item span[title='{region}']").find_element(By.XPATH, './..')
    
    def close_change_region_time(self, region, time):
        selector = f".sbis_ru-Region-Panel__container [title='{region}']"
        WebDriverWait(self.browser, time).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, selector))
        )