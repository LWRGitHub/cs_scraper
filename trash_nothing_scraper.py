from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time

# set old data
# r = requests.get("https://trashnothing.com/beta/browse?radius=160934&search=apple")
# soup = bs(r.content)
# old_data = soup.find_all("a", attrs={"class": "offer"})
old_data = []
count = 0
print(len(old_data))
while True:
    # get new data
    r = requests.get("https://trashnothing.com/beta/browse?radius=160934&search=apple")
    soup = bs(r.content)
    recent_data = soup.find_all("a", attrs={"class": "offer"})

    count += 1
    # print(count)

    if old_data != recent_data:
        new_href = []
        old_href = []

        print("--------------------- recent_data ------------------ ")
        print(recent_data)
        print("--------------------- /recent_data ------------------ ")

        # for tag in recent_data:
        #     print("--------------------- tag ------------------ ")
        #     print(type(tag))
        #     print("--------------------- /tag ------------------ ")
        #     new_href.append(tag.find("a")['href'])
        #     # name.append(tag.fint())

        # for tag in old_data:
        #     old_href.append(tag.find("a")['href'])

        # print("--------------------- Compair old & new ------------------ ")
        # print("--------------------- old ------------------ ")
        # print(recent_data)
        # print("--------------------- /old ------------------ ")
        # print("--------------------- new ------------------ ")
        # print(old_data)
        # print("--------------------- /new ------------------ ")
        # print("--------------------- /Compair old & new ------------------ ")

        # ---------------------text 1------------------------
        # tex1 = ""
        # for data1 in recent_data:
        #     if data1 not in old_data:
        #         print("--------------------- Data that changed ------------------ ")
        #         print(data1)
        #         print("--------------------- /Data that changed ------------------ ")

        PATH = "/Users/codetenderloin/dev/chromedriver"
        driver = webdriver.Chrome(PATH)

        driver.get("https://messages.textfree.us/login")

        time.sleep(2)
        # username
        username = driver.find_element_by_name("username")
        username.send_keys("")

        # password
        password = driver.find_element_by_name("password")
        password.send_keys("")

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
        contactInput.send_keys("4155738950")

        #click to input message
        emojionearea_editor = driver.find_element_by_class_name('emojionearea-editor')

        #add message
        emojionearea_editor.send_keys('Trash Nothing Data Changed "Apple", https://trashnothing.com/beta/browse?radius=160934&search=apple')

        #send
        sendButton = driver.find_element_by_id('sendButton')
        sendButton.click()

        time.sleep(2)
        driver.quit()
        # ---------------------/text 1------------------------
        old_data = recent_data

        # for data_id in new_href:
        #     if data_id not in old_href:
        #         new_a = []
        #         old_a = []
        #         # name = []
        #         for tag in recent_data:
        #             new_a.append(tag.find("a")['href'])
        #             # name.append(tag.fint())

        #         for tag in old_data:
        #             old_a.append(tag.find("a")['href'])

        #         # print(new_a)
        #         # print(old_a)

        #         message_to_send = ''
        #         for href1 in new_a:
        #             if href1 not in old_a:
        #                 message_to_send = href1
                
        #         print("----------------message----------------")
        #         print(message_to_send)
        #         print("----------------/message----------------")

        #         old_data = recent_data

        #         PATH = "/Users/codetenderloin/dev/chromedriver"
        #         driver = webdriver.Chrome(PATH)

        #         driver.get("https://messages.textfree.us/login")

        #         time.sleep(2)
        #         # username
        #         username = driver.find_element_by_name("username")
        #         username.send_keys("")

        #         # password
        #         password = driver.find_element_by_name("password")
        #         password.send_keys("")

        #         #log in btn
        #         log_in_btn = driver.find_element_by_class_name('button-purple')
        #         log_in_btn.click()

        #         time.sleep(2)
        #         #close pop up
        #         SyncContactsXDismissPopup = driver.find_element_by_id('SyncContactsXDismissPopup')
        #         SyncContactsXDismissPopup.click()

        #         # selevxt startNewConversationButton
        #         startNewConversationButton = driver.find_element_by_id('startNewConversationButton')
        #         startNewConversationButton.click()

        #         #number input
        #         contactInput = driver.find_element_by_id('contactInput')
        #         contactInput.send_keys("4155738950")

        #         #click to input message
        #         emojionearea_editor = driver.find_element_by_class_name('emojionearea-editor')

        #         if message_to_send != '':
        #             emojionearea_editor.send_keys(f"https://trashnothing.com/beta/browse?radius=160934&search=apple Check Trash Nothing Apple stuff! {message_to_send}")
        #         else:
        #             emojionearea_editor.send_keys('Something is wrong with Trash Nothing Apple bot https://trashnothing.com/beta/browse?radius=160934&search=apple')

        #         #send
        #         sendButton = driver.find_element_by_id('sendButton')
        #         sendButton.click()

        #         time.sleep(2)
        #         driver.quit()
            # else:
            #     old_data = recent_data
 

    time.sleep(2)