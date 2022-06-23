from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions


# Function to parse input from buy items and returns only the price as a int
def get_element_amount_to_int(element):
    input_str = element.text
    out_int = None
    try:
        input_str = (input_str.split("- "))[1]
        input_str = input_str.split("\n")[0]
        out_int = int(input_str.replace(",", ""))
    except IndexError:
        out_int = int(input_str.replace(",", ""))
    finally:
        return out_int

class Game(Service):

    def __init__(self):
        super().__init__()

        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(30)
        self.driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
        self.wait = WebDriverWait(self.driver, 60)
        self.money = None
        self.money_amount = 0
        self.big_cookie = None
        self.cps = None
        self.cps_amount = 0

        self.upgrades = {
            "cursor": {"element": None, "price": None, "selector": "buyCursor"},
            "grandma": {"element": None, "price": None, "selector": "buyGrandma"},
            "factory": {"element": None, "price": None, "selector": "buyFactory"},
            "mine": {"element": None, "price": None, "selector": "buyMine"},
            "shipment": {"element": None, "price": None, "selector": "buyShipment"},
            "alchemy": {"element": None, "price": None, "selector": "buyAlchemy lab"},
            "portal": {"element": None, "price": None, "selector": "buyPortal"},
            "time_machine": {"element": None, "price": None, "selector": "buyTime machine"},
        }

        # Functions
        self.get_elements()
        self.get_money()

    # def find(self, id_selector):
    #     elements = self.driver.find_elements(by=By.ID, value=id_selector)
    #     if elements:
    #         return elements
    #     else:
    #         return False

    def get_element_by_id_selector(self, id_selector):
        elements = self.driver.find_element(by=By.ID, value=id_selector)
        return elements

    def get_elements(self):

        for n in self.upgrades:
            self.upgrades[n]["element"] = self.get_element_by_id_selector(self.upgrades[n]["selector"])
        print(self.upgrades)

        self.big_cookie = self.get_element_by_id_selector(id_selector="cookie")

        self.cps = self.get_element_by_id_selector(id_selector="cps")

        self.money = self.get_element_by_id_selector(id_selector="money")

    def get_upgrade_prices(self):
        print("getting upgrade prices")
        self.get_elements()
        for n in self.upgrades:
            self.upgrades[n]["price"] = get_element_amount_to_int(self.upgrades[n]["element"])
            print(n, self.upgrades[n]["price"])

    def get_money(self):
        self.get_elements()
        self.money_amount = get_element_amount_to_int(self.money)
        print(f"My Money:{self.money_amount}")

    def get_cps(self):
        self.get_elements()
        cps_string=self.cps.text
        self.cps_amount=cps_string.split(":")[1]
        print(self.cps_amount)

    def buy_upgrade(self):
        self.get_elements()
        
        for n in reversed(self.upgrades):
            if self.upgrades[n]["price"] <= self.money_amount:
                print(f"enough money for:{n}")
                succeed = False
                while not succeed:
                    try:
                        self.wait.until(ec.element_to_be_clickable(self.upgrades[n]["element"])).click()
                        succeed = True
                        print("success")
                    except:
                        print(f"element not found:{n}")
                        self.get_upgrade_prices()
                        pass
                print(f"enough money for:{n}")
                #
                # self.upgrades[n]["element"].click()
