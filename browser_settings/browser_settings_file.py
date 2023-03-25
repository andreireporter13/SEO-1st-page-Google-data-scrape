#
#
#
# This file have more settings for scraper's firefox browser

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#
from selenium.webdriver.common.proxy import Proxy, ProxyType
#
#
#
def configured_driver(proxy_data: str, user_agent: str): 
    """ This function configure webdriver! """

    ### PROXY
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': f'{proxy_data}',
        'sslProxy': f'{proxy_data}'
    })
    ###
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    # 
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.set_capability('useAutomationExtension', False)
    options.set_capability("excludeSwitches", ["enable-automation"])

    ### proxy here
    options.proxy = proxy

    ### USER AGENT 
    options.set_preference("general.useragent.override", user_agent) 

    ### OPTIONS HEADLESS
    # with this argument, browser work in background
    #options.add_argument('-headless')

    # set path to firefox driver;
    firefox_service = Service(executable_path="/home/linuxtramp/Documents/Python3_projects/Paunica_SEO_project/Firefox_Driver/geckodriver")
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver



####################
driver = configured_driver('localhost:8118', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0')

try: 
    from time import sleep
    driver.get('https://www.whatsmyip.org/')

except Exception as ex:
    print(ex)

finally: 
    sleep(10)
    driver.close()
    driver.quit()
