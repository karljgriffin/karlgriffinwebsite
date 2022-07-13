from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import environ
from time import sleep

browser = webdriver.Chrome("/Users/karlgriffin/Downloads/chromedriver-4")
browser.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")

done = False

while not done:

    try:
        # Click on button for booking
        browser.find_element_by_xpath('//*[@id="SW300-1|4"]/td[6]/a').click()

        sleep(1)

        # Click on accept cookies
        browser.find_element_by_xpath(
            '//*[@id="onetrust-accept-btn-handler"]').click()

        # Enter UCD number and press Return
        browser.find_element_by_xpath(
            '//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]').send_keys(environ.get('student_number'), Keys.RETURN)

        sleep(1)

        # Click on confirm booking
        browser.find_element_by_xpath(
            '//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]').click()

        done = True

    except:
        print("Attempting to book...")
        sleep(1)
        browser.refresh()

# Wait 10 seconds and close
sleep(10)
browser.quit()


# To store environment variable permanently on computer:
# open terminal, type 'nano .bash_profile', assign variable like name="Karl", control+X & Enter, close terminal and open again
