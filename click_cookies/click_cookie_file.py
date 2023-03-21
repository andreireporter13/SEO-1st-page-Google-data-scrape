#
#
#
# This script will be click on Cookie automated...
#
#
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from time import sleep
#
import re
#
#import re
#
#
def accept_cookies_regex() -> list:
    """ 
    This function return a list of regex 
    for searching in cookies buttons.
    """ 
    cookies_accept = [

                        # for Accept or Accept all word
                        re.compile(r"\W*[Aa][Cc]+[Ee][Pp][Tt][A-Za-z\s\d]*\W*\s*.*"),

                        # for Permite or Permite toate word
                        re.compile(r"\W*[Pp][Ee][Rr][Mm][Ii][Tt][Ee]+\W*\s*.*"),

                        # Da, accept 
                        re.compile(r"[Dd][Aa],\s+[Aa][Cc][Cc][Ee][Pp][Tt]$"),

                        # regex for I accept all 
                        re.compile(r"\b[iI]\s*[Aa][Cc][Cc][Ee][Pp][Tt]\s+[Aa][Ll][Ll]\b"),

                        # regex for Save and Close 
                        re.compile(r"\s*(s|S)(A|a)(V|v)(E|e)\s+(A|a)(N|n)(D|d)\s+(c|C)(L|l)(O|o)(S|s)(E|e)\s*"),

                        # for ok
                        re.compile(r"\W*[Oo][Kk]+\W*\s*.*"),

                        # for continue with recommended cookies
                        re.compile(r"\W*[Cc][Oo][Nn][Tt][Ii][Nn][Uu][Ee]\W*\s*[Ww][Ii][Tt][Hh]\s+\w*\s*[Rr][Ee][Cc][Oo][Mm][Mm][Ee][Nn][Dd][Ee][Dd]\s+[Cc][Oo][Oo][Kk][Ii][Ee][Ss]\W*\s*.*"),

                        # for Bine, sunt de acord
                        re.compile(r"\W*[Bb][Ii][Nn][Ee]\W*\s*\,\s*\W*[Ss][Uu][Nn][Tt]\W*\s*\W*[Dd][Ee]\W*\s*\W*[Aa][Cc][Oo][Rr][Dd]\W*\W*\s*.*"),

                        # for Go it
                        re.compile(r"\W*[Gg][Oo]\s*[Ii][Tt]\W*\s*"),

                        # for Sunt de acord
                        re.compile(r"\S*[Ss][Uu][Nn][Tt]\W*[Dd][Ee]\W*[Aa][Cc][Oo][Rr][Dd]\S*"),

                        #
    ]

    # 
    return cookies_accept


# 
def search_buttons_by_regex_and_click_cookies(driver) -> None:
    """ 
    This func() search CoockieButton in HTML elements.
    Selenium objects decode in HTML, HTML verify with regex and, if something found, 
    click on selenium object.
    """

    # catch all buttons from this site
    try:

        # by Buttons
        elements_by_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.XPATH, "//button"))
                        )

        # search in elements_by_button
        for elem in elements_by_button:

            # text from elem
            text = driver.execute_script("return arguments[0].innerHTML;", elem)

            # search in regex
            for btn in accept_cookies_regex():
                if re.search(btn, text):
                    #elem.click()
                    driver.execute_script("arguments[0].click();", elem)
                    sleep(0.5)

                    break
        else: 
            # secret "for" for tag a
            elements_by_a = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//a"))
                    )
            for elem_2 in elements_by_a:
                
                # text from elem
                text = driver.execute_script("return arguments[0].innerHTML;", elem_2)

                for btnn in accept_cookies_regex():
                    if re.search(btnn, text):
                        #elem_2.click()
                        driver.execute_script("arguments[0].click();", elem_2)
                        sleep(0.5)

                        break

    except Exception as ex:
        print(ex)

