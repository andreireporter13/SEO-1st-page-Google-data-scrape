#
#
#
# Script for SEO Automation ---> 
# This script can return rezults from Google
#
# Author - Andrei C. Cojocaru - number1101
# website - https://webautomation.ro
#
#
#
# main module, Firefox configured
from browser_settings import configured_driver
from click_cookies import search_buttons_by_regex_and_click_cookies
#
from GUI_for_App import layout
#
# this module save data to CSV 
from save_list_to_csv import save_data_to_csv_files
#
# main module, but googlesearch-python project
from Google_Search import GoogleSearch
#
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#
# python3 packages
from time import sleep
import re
import datetime
from random import randint
#
import PySimpleGUI as sg
#
#
#
################################################# START CODE ----> ENGINE HERE <---- ####################################################
#
#
#
def return_links_from_google(seo_keyword: str) -> list:
    """ 
    This func() return all links from Google. This func call 
    my class with googlesearch-python in it.
    """
    
    first_page_links = GoogleSearch(seo_keyword)

    # return links
    return first_page_links.search_by_keyword()
#
#
def scrap_data_from_links(driver, list_with_links: list) -> list:
    """ 
    This function use Selenium Webdriver and BS4 for scraping data from
    web pages.
    """ 
    
    data_from_google_links = []
    for link in list_with_links: 

        # all h2 
        h2_list = []

        # all h3
        h3_list = []

        #
        driver.get(link)
        driver.implicitly_wait(10)  # wait for totaly load page

        ############# DO CLICK ON COOKIES BUTTONS WITH MAIN IMPORTED MODULE ##################
        sleep(1)
        search_buttons_by_regex_and_click_cookies(driver)
        sleep(1)
        ######################################################################################

        # make soup object
        soup_data = BeautifulSoup(driver.page_source, 'lxml')

        # time to extrat data from webpage
        Site = link

        try: 
            H1 = soup_data.title.text.strip()
        except: 
            H1 = '-'
        
        try:

            H2 = soup_data.find_all("h2")
            if H2: 
                for data in H2:
                    h2_list.append(data.text.strip())
        except: 
            H2 = '-'
        
        try:
            H3 = soup_data.find_all("h3")
            if H3: 
                for data in H3:
                    h3_list.append(data.text.strip())
        except: 
            H3 = '-'

        try: 
            Meta_content = soup_data.find('meta', attrs={'name': 'description'})['content']
        except:
            Meta_content = '-'
        
        try: 
            Meta_description = soup_data.find('meta', attrs={'name': 'content'})['content']
        except:
            Meta_description = '-'

        data_from_google_links.append([Site, H1, h2_list, h3_list, Meta_content, Meta_description])

        # sleep, for better work
        sleep(randint(2, 4))

    print(data_from_google_links)

    # return data, and prepare it to save in CSV file
    #
    return data_from_google_links


def main():
    """ 
    This func() store all function about this project.
    """
    
    window = sg.Window("Free scraping SEO app", layout, size=(1150, 600))

    ########################### DEFAULT VALUES #########################################
    default_proxy = 'localhost'
    default_user_agent = 'Mozilla/5.0'
    ####################################################################################
    #
    ########################## VALUES TO STORE DATA ####################################
    proxy_settings = default_proxy
    user_agent_settings = default_user_agent
    ####################################################################################

    


    ### GO IN WHILE LOOP
    while True:

        # read values
        event, values = window.read()

        # for close
        if event is None or event == 'Exit':
            break;

        # Documentation from menu
        elif event == 'Documentation':
            doc_layout = [[sg.Text('Documentation DATA', font=('Arial', 20), justification='center')],
                    [sg.HorizontalSeparator()],
                    [sg.Text('Cod saved on:', font=('Arial', 12)), sg.Text('Github.com', font=('Arial', 12))],
                    [sg.Text('License:', font=('Arial', 12)), sg.Text('MIT', font=('Arial', 12))],
                    [sg.Text('Doc_link:', font=('Arial', 12)), sg.Text('Here', font=('Arial', 12))],
                    [sg.HorizontalSeparator()],
                    [sg.Button('OK', size=(10, 1), pad=((200, 0), (20, 20)))]]

            doc_window = sg.Window('Documentation', doc_layout)

            while True:
                event, values = doc_window.read()

                if event in (sg.WIN_CLOSED, 'OK'):
                        break

                doc_window.close()

         # Open a window for details
        elif event == 'Details':
            doc_layout = [[sg.Text('Free SEO App', font=('Arial', 20), justification='center')],
                    [sg.HorizontalSeparator()],
                    [sg.Text('Version:', font=('Arial', 12)), sg.Text('1.0', font=('Arial', 12))],
                    [sg.Text('Author:', font=('Arial', 12)), sg.Text('Andrei C. Cojocaru', font=('Arial', 12))],
                    [sg.Text('Description:', font=('Arial', 12)), sg.Text('Open Source Application', font=('Arial', 12))],
                    [sg.HorizontalSeparator()],
                    [sg.Button('OK', size=(10, 1), pad=((200, 0), (20, 20)))]]

            doc_window = sg.Window('Details', doc_layout)

            while True:
                event, values = doc_window.read()

                if event in (sg.WIN_CLOSED, 'OK'):
                    break

            doc_window.close()

        # Open a window for setting Proxy
        elif event == 'Set Proxy':
            proxy_layout = [[sg.Text('Insert proxy data:')],
                            [sg.Text('IP:'), sg.InputText()],
                            [sg.Text('Port:'), sg.InputText()],
                            [sg.Button('OK')]]

            proxy_window = sg.Window('Set Proxy', proxy_layout)
                
            while True:
                event, values = proxy_window.read()

                if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
                    break

                # save proxy settings
                elif event == 'OK':
                    proxy_ip = values[0]
                    proxy_port = values[1]

                    proxy_settings = f'{proxy_ip}:{proxy_port}'
                    sg.popup(f'Setările proxy-ului au fost salvate: {proxy_settings}')
                    proxy_window.close()


        # Open a window to set UserAgent
        elif event == 'Set UserAgent':
            ua_layout = [[sg.Text('Insert User Agent')],
                    [sg.InputText()],
                    [sg.Button('OK')]]

            ua_window = sg.Window('User Agent settings', ua_layout)

            while True:
                event, values = ua_window.read()

                if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
                    break

                # Salvează setările User Agent
                elif event == 'OK':
                    user_agent_settings = values[0]

                    # Salvează setările și închide fereastra
                    # (aici ar trebui să adaugi codul tău pentru a salva datele)
                    sg.popup(f'User Agent settings was saved: {user_agent_settings}')
                    ua_window.close()

        # Open a window for website
        elif event == 'Website':
            website_layout = [[sg.Text('Visit our website:')],
                            [sg.Text('https://webautomation.ro')],
                            [sg.Button('OK')]]

            website_window = sg.Window('Website', website_layout)

            while True:
                event, values = website_window.read()

                if event in (sg.WIN_CLOSED, 'OK'):
                    website_window.close()  # inchide fereastra
                    break

        # Open a contact form
        elif event == 'Email':
            website_layout = [[sg.Text('Contact as via email:')],
                            [sg.Text('contact@webautomation.ro')],
                            [sg.Button('OK')]]

            website_window = sg.Window('Website', website_layout)

            while True:
                event, values = website_window.read()

                if event in (sg.WIN_CLOSED, 'OK'):
                    website_window.close()  # inchide fereastra
                    break

        ############################################################################################################
        ################################## START RUN SCRIPT ########################################################
        ############################################################################################################
        
        elif event == 'Run Scraper':
            
            # data from input
            keywords = values.get('-IN-', '').split(',')

            # check if keywords
            if keywords[0] == '':
                sg.popup('Please enter at least one keyword.')
            elif len(keywords) > 3:
                sg.popup('Please enter no more than 3 keywords.')
            else:
                for keyword in keywords:
                    for i in range(1000):
                        event, values = window.read(timeout=10)
                        if event == sg.WIN_CLOSED:
                            break
                        elif event == 'Cancel':
                            if sg.popup_ok_cancel('Do you really want to stop the scraper?') == 'OK':
                                sg.popup('Scraper stopped.')
                                return
                        sleep(0.01)
                        sg.OneLineProgressMeter(f'Scrape: |{keyword}|', i+1, 1000, 'ScraperMeter')

                        # here need insert all logic of code.
                        # set proxy and user_agent
                        # and ignore pycache

    window.close()


if __name__ == "__main__":
    main()
