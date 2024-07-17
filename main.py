import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Actions import Actions



if __name__ == "__main__":
    driver = webdriver.Edge()
    url = "https://www.meteored.mx/clima_Torreon-America+Norte-Mexico-Coahuila-MMTC-1-22375.html"
    driver.implicitly_wait(0.3)
    # actions = [
    #     {"action": "openUrl"},
    #     {"action": "sendKeys", "locator_type": "xpath", "locator": "//input[@name='email']", "keys": "crismoo3012@gmail.com"},
    #     {"action": "sendKeys", "locator_type": "xpath", "locator": "//input[@name='password']", "keys": "monarcaazul123"},
    #     {"action": "click", "locator_type": "xpath", "locator": "//button[@type='submit']"},
    #     {"action": "close"}
    # ]
    actions = [
        {"action": "openUrl"},
        {"action": "get_elements_by_locator", "locator_type": "xpath", "locator": "//ul[contains(@class, 'grid-container-7') and contains(@class, 'dias_w')]"},
    ]
    
    
    action_executor = Actions(driver, url, actions)
    action_executor.execute()
    action_executor.dataFrame.to_excel("data.xlsx", index=False)