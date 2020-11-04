from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time

# set old data
r = requests.get("https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal=94102")
soup = bs(r.content)
old_data = soup.find_all("h3", attrs={"class": "result-heading"})
# old_data = []
all_herf = []
for tag in old_data:
    all_herf.append(tag.find("a")['href'])
count = 0

while True:
    # get new data
    r = requests.get("https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal=94102")
    soup = bs(r.content)
    h3 = soup.find_all("h3", attrs={"class": "result-heading"})

    # print(old_data)
    # if old_data != []:
    #     old_data = h3
    # print(old_data)

    count += 1
    # print(count)

    if old_data != h3:
        # new_id = []
        # old_id = []
        new_herf = []
        # old_herf = []
        

        for tag in h3:
            # new_id.append(tag.find("a")['data-id'])
            new_herf.append(tag.find("a")['href'])

        # for tag in old_data:
        #     old_id.append(tag.find("a")['data-id'])
        #     old_herf.append(tag.find("a")['href'])

        print("--------------------- Compair old & new ------------------ ")
        print("--------------------- old ------------------ ")
        print(h3)
        print("--------------------- /old ------------------ ")
        print("--------------------- new ------------------ ")
        print(old_data)
        print("--------------------- /new ------------------ ")
        print("--------------------- /Compair old & new ------------------ ")

        # ---------------------text 1------------------------
        # tex1 = ""
        for data1 in h3:
            if data1 not in old_data:
                print("--------------------- Data that changed ------------------ ")
                print(data1)
                print("--------------------- /Data that changed ------------------ ")

        PATH = "/home/logan/Desktop/dev/chromedriver"
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
        emojionearea_editor.send_keys('Data Changed Craigslist Apple, https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal=94102')

        #send
        sendButton = driver.find_element_by_id('sendButton')
        sendButton.click()

        time.sleep(2)
        driver.quit()
        # ---------------------/text 1------------------------

        # there_is_a_new_id = False
        there_is_a_new_herf = False
        # for data_id in new_id:
        #     if data_id not in old_id:
        #         there_is_a_new_id = True

        message_to_send = ''
        for data_href in new_herf:
            if data_href not in all_herf:
                there_is_a_new_herf = True
                message_to_send += data_href
                all_herf.append(data_href)

        
        if there_is_a_new_herf:
            
            print("----------------message----------------")
            print(message_to_send)
            print("----------------/message----------------")

            old_data = h3

            # PATH = "/Users/codetenderloin/dev/chromedriver"
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

            if message_to_send != '':
                emojionearea_editor.send_keys(f"https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal=94102 Check Craigslist Apple stuff! {message_to_send}")
            else:
                emojionearea_editor.send_keys('Something is wrong with Craigslist Apple bot https://sfbay.craigslist.org/search/zip?query=apple&search_distance=100&postal=94102')

            #send
            sendButton = driver.find_element_by_id('sendButton')
            sendButton.click()

            time.sleep(2)
            driver.quit()
        else:
            old_data = h3

    time.sleep(2)