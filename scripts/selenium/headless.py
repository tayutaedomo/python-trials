import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)

    url = 'https://yahoo.co.jp'
    driver.get(url)

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tmp', 'capture.png')
    driver.save_screenshot(file_path)

    #browser.quit()

