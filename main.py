import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

def get_cel_details(cel):
    try:
        name = cel.find_element(By.CSS_SELECTOR, '.ui-search-item__title').text
    except Exception:
        name = "N/A"

    try:
        price = cel.find_element(By.CSS_SELECTOR, '.ui-search-price__part--medium').text
    except Exception:
        price = "N/A"

    try:
        url = cel.find_element(By.CSS_SELECTOR, 'a.ui-search-link').get_attribute('href')
    except Exception:
        url = "N/A"

    return {
        'name': name,
        'price': price,
        'url': url
    }

if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get('https://www.mercadolibre.com.mx/')

    search_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'nav-search-input'))
    )

    search_box.send_keys('Celulares')
    search_box.submit()

    list_celphones = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.ui-search-layout__item'))
    )

    cel_details = [get_cel_details(cel) for cel in list_celphones]

    df = pd.DataFrame(cel_details)
    df.to_excel('celulares.xlsx', index=False)

    driver.quit()
