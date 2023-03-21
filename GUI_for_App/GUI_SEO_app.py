#
#
#
#
#
# GUI For Desktop SEO App --->>> 
# PySimpleGUI is the best!!! 
# BEST!
#
#
#
#
#
import PySimpleGUI as sg
import time
#
#
# app theeme 
sg.theme('DarkBlue13')

# menu app ---> data
menu_app = [
                ["Info", ["Documentation", "Details", "---", "Exit"]],
                ["User Agent", ["Set UserAgent"]],
                ["Proxy", ["Set Proxy"]],
                ["Contact", ["Website", "Email"]],
        ]       
#
#
# layout data
layout = [       
                # for menu data
                [sg.Menu(menu_app, key="-MENU-")],

                # for banner https://webautomation.ro
                [sg.Image("/home/linuxtramp/Documents/Python3_projects/Paunica_SEO_project/GUI_for_App/img/seo_app_banner.png"),],

                # title
                [sg.Frame('',[[sg.Text('This app scrape data from first pages in Google and store data in CSV files.', size=(0, 0), 
                font='Any 15', justification='center')]], pad=((230,50),(15,30)))],

                # label for input data: keywords for search
                [sg.Text('Insert keywords here, separated by commas. (Max-3):', font="Any 15", justification='center', pad=((320, 0), (10, 0)))],
                [sg.InputText(key='-IN-', size=(70, 10), pad=((260, 0), (10, 0)), border_width=1, font='Any 12')],

                # Run Scraper and Cancel button
                [sg.Button('Run Scraper', button_color=('white', 'blue'), size=(10,1), font='Any 15', pad=((430, 0), (30, 0))), sg.Button('Cancel', button_color=('white', 'blue'), size=(10,1), font='Any 15', pad=((20, 100), (30, 0)))],

        ]

