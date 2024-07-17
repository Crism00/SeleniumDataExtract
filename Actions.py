import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time

class Actions:
    def __init__(self, driver, url, actions=[]):
        self.driver = driver
        self.url = url
        self.actions = actions
        self.dataFrame = pd.DataFrame()
        
    def open_url(self):
        self.driver.get(self.url)
    
    def click_on_element(self, element):
        element.click()
        
    def get_element_by_class(self, locator):
        return self.driver.find_element(By.CLASS_NAME, locator)
    
    def get_element_by_id(self, locator):
        return self.driver.find_element(By.ID, locator)
    
    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)
        
    def send_keys(self, element, keys):
        element.send_keys(keys)
        
    def obtain_element_text(self, element):
        return element.text
    
    def close(self):
        self.driver.close()
    
    def read_json(self, file):
        with open(file) as f:
            data = json.load(f)
        return data
    
    def execute(self):
        for action in self.actions:
            time.sleep(1.25)
            if action['action'] == 'click':
                element = self.get_element_by_locator(action)
                self.click_on_element(element)
            elif action['action'] == 'sendKeys':
                element = self.get_element_by_locator(action)
                self.send_keys(element, action['keys'])
            elif action['action'] == 'openUrl':
                self.open_url()
            elif action['action'] == 'close':
                time.sleep(2)
                self.close()
            elif action['action'] == 'obtain_element_text':
                element = self.get_element_by_locator(action)
                self.dataFrame = pd.DataFrame([self.obtain_element_text(element)])
            elif action['action'] == 'obtain_list_items':
                elements = self.get_elements_by_locator(action)
                items = self.obtain_list_items(elements)
                self.dataFrame = pd.DataFrame(items)
            elif action['action'] == 'get_elements_by_locator':
                elements = self.get_elements_by_locator(action)
                contador = 0

                    
                    
    # Método para obtener texto de cada elemento de una lista
    def obtain_list_items(self, elements):
        items = []
        for element in elements:
            items.append(element.text)
        return {'items': items}  # Devuelve un diccionario con los items obtenidos
                
    def get_element_by_locator(self, action):
        locator_type = action.get('locator_type', 'xpath')
        locator = action['locator']
        
        if locator_type == 'id':
            return self.get_element_by_id(locator)
        elif locator_type == 'class':
            return self.get_element_by_class(locator)
        elif locator_type == 'xpath':
            return self.get_element(locator)
        elif locator_type == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        else:
            raise ValueError(f"Unknown locator type: {locator_type}")
        
    def get_elements_by_locator(self, action):
        locator_type = action.get('locator_type', 'xpath')
        locator = action['locator']
        
        if locator_type == 'id':
            return self.driver.find_elements(By.ID, locator)
        elif locator_type == 'class':
            return self.driver.find_elements(By.CLASS_NAME, locator)
        elif locator_type == 'xpath':
            return self.driver.find_elements(By.XPATH, locator)
        elif locator_type == 'css':
            return self.driver.find_elements(By.CSS_SELECTOR, locator)
        else:
            raise ValueError(f"Unknown locator type: {locator_type}")