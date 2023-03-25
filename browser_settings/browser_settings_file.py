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

    ### set proxy here
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

    ### USER AGENT 
    options.set_preference("general.useragent.override", user_agent) 

    ### OPTIONS HEADLESS
    #options.add_argument('-headless')

    if '127.0.0.1' in proxy_data or 'localhost' in proxy_data:
        # here driver work without proxy...
        #...

        # set path to firefox driver;
        firefox_service = Service(executable_path="/home/linuxtramp/Documents/Python3_projects/Paunica_SEO_project/Firefox_Driver/geckodriver")
        driver = webdriver.Firefox(service=firefox_service, options=options)

        return driver

    else: 
        # here driver work with proxy...
        #...

        ### proxy here
        options.proxy = proxy

        # set path to firefox driver;
        firefox_service = Service(executable_path="/home/linuxtramp/Documents/Python3_projects/Paunica_SEO_project/Firefox_Driver/geckodriver")
        driver = webdriver.Firefox(service=firefox_service, options=options)

        return driver

