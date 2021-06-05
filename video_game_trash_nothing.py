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
RADIAOUS = os.getenv('TRASH_NOTHING_RADIAOUS')

# set old data
r = requests.get(f"https://trashnothing.com/beta/browse?search=video%20game&radius={RADIAOUS}")
soup = bs(r.content)
old_data = soup.find_all("a", attrs={"class": "offer"})

# uncomment `old_data` to recive all items when you first run the app
# old_data = []

all_herf = []
for a in old_data:
    all_herf.append(a['href'])
print(all_herf)

while True:
    # get new data
    r = requests.get(f"https://trashnothing.com/beta/browse?search=video%20game&radius={RADIAOUS}")
    soup = bs(r.content)
    recent_data = soup.find_all("a", attrs={"class": "offer"})

    if old_data != recent_data:
        new_href = []

        print("--------------------- recent_data ------------------ ")
        print(recent_data)
        print("--------------------- /recent_data ------------------ ")

        for a in recent_data:
            print("------------- a -----------")
            print(a['href'])
            print("------------- /a -----------")
            new_href.append(a['href'])

        print("--------------------- Compair old & new ------------------ ")
        print("--------------------- old ------------------ ")
        print(recent_data)
        print("--------------------- /old ------------------ ")
        print("--------------------- new ------------------ ")
        print(old_data)
        print("--------------------- /new ------------------ ")
        print("--------------------- /Compair old & new ------------------ ")

        there_is_a_new_href = False

        message_to_send = ''
        for data_href in new_href:
            if data_href not in all_herf:
                there_is_a_new_href = True
                message_to_send += f"https://trashnothing.com{data_href} "
                all_herf.append(data_href)

        
        if there_is_a_new_href:
            # new_a = []
            
            print("----------------message----------------")
            print(message_to_send)
            print("----------------/message----------------")

            old_data = recent_data

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
                emojionearea_editor.send_keys(f"https://trashnothing.com/beta/browse?search=video%20game&radius={RADIAOUS} Check Trash Nothing Video Game stuff! {message_to_send}")
            else:
                emojionearea_editor.send_keys(f'Something is wrong with Trash Nothing Video Game bot https://trashnothing.com/beta/browse?search=video%20game&radius={RADIAOUS}')

            #send
            sendButton = driver.find_element_by_id('sendButton')
            sendButton.click()

            time.sleep(2)
            driver.quit()
        else:
            old_data = recent_data
 

    time.sleep(2)