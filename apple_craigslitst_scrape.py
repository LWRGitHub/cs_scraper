from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from dotenv import load_dotenv
import os

load_dotenv()

TEXT_FREE_USERNAME = os.getenv('TEXT_FREE_USERNAME')
TEXT_FREE_PASS = os.getenv('TEXT_FREE_PASS')
MSM_NUM = os.getenv('MSM_NUM')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
ZIP_TO_SEARCH_AROUND = os.getenv('CRAIGSLIST_ZIP')

# set old data
r = requests.get(f"https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal={ZIP_TO_SEARCH_AROUND}")
soup = bs(r.content)
old_data = soup.find_all("h3", attrs={"class": "result-heading"})

# uncomment `old_data` to recive all items when you first run the app
old_data = []

all_href = []
for tag in old_data:
    all_href.append(tag.find("a")['href'])

while True:
    # get new data
    r = requests.get(f"https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal={ZIP_TO_SEARCH_AROUND}")
    soup = bs(r.content)
    h3 = soup.find_all("h3", attrs={"class": "result-heading"})

    if old_data != h3:
        new_href = []
        

        for tag in h3:
            new_href.append(tag.find("a")['href'])

        print("--------------------- Compair old & new ------------------ ")
        print("--------------------- old ------------------ ")
        print(h3)
        print("--------------------- /old ------------------ ")
        print("--------------------- new ------------------ ")
        print(old_data)
        print("--------------------- /new ------------------ ")
        print("--------------------- /Compair old & new ------------------ ")

        for data1 in h3:
            if data1 not in old_data:
                print("--------------------- Data that changed ------------------ ")
                print(data1)
                print("--------------------- /Data that changed ------------------ ")
        
        there_is_a_new_href = False

        message_to_send = ''
        for data_href in new_href:
            if data_href not in all_href:
                there_is_a_new_href = True
                message_to_send += data_href
                all_href.append(data_href)

        
        if there_is_a_new_href:
            
            print("----------------message----------------")
            print(message_to_send)
            print("----------------/message----------------")

            old_data = h3

            driver = webdriver.Chrome(CHROME_DRIVER_PATH)

            driver.get("https://messages.textfree.us/login")

            time.sleep(2)
            # username
            username = driver.find_element_by_name("username")
            username.send_keys(TEXT_FREE_USERNAME)

            # password
            password = driver.find_element_by_name("password")
            password.send_keys(TEXT_FREE_PASS)

            #log in btn
            log_in_btn = driver.find_element_by_class_name('button-purple')
            log_in_btn.click()

            time.sleep(2)
            #close pop up
            SyncContactsXDismissPopup = driver.find_element_by_id('SyncContactsXDismissPopup')
            SyncContactsXDismissPopup.click()

            # selevxt startNewConversationButton
            startNewConversationButton = driver.find_element_by_id('startNewConversationButton')
            startNewConversationButton.click()

            #number input
            contactInput = driver.find_element_by_id('contactInput')
            contactInput.send_keys(MSM_NUM)

            #click to input message
            emojionearea_editor = driver.find_element_by_class_name('emojionearea-editor')

            if message_to_send != '':
                emojionearea_editor.send_keys(f"https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal={ZIP_TO_SEARCH_AROUND} Check Craigslist Apple stuff! {message_to_send} ")
            else:
                emojionearea_editor.send_keys(f'Something is wrong with Craigslist Apple bot https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal={ZIP_TO_SEARCH_AROUND}')

            #send
            sendButton = driver.find_element_by_id('sendButton')
            sendButton.click()

            time.sleep(2)
            driver.quit()
        else:
            old_data = h3

    time.sleep(2)