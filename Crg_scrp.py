from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from Env import Env


class Crg_scrp:
    
    def __init__(self, look_for):
        # dotenv
        self.env = Env()
        self.look_for = look_for.lower()

        # bs4
        # set old data
        self.r = requests.get(f"https://sfbay.craigslist.org/search/zip?query={look_for}&search_distance={self.env.DISTANCE}&postal={self.env.CRAIGSLIST_ZIP}")
        self.soup = bs(self.r.content)
        self.old_data = self.soup.find_all("h3", attrs={"class": "result-heading"})
    

    def indefinite_scrp(self):
        # uncomment `old_data` to recive all items when you first run the app
        self.old_data = []

        all_href = []
        for tag in self.old_data:
            all_href.append(tag.find("a")['href'])

        while True:
            # get new data
            r = requests.get(f"https://sfbay.craigslist.org/search/zip?query={self.look_for}&search_distance={self.env.DISTANCE}&postal={self.env.CRAIGSLIST_ZIP}")
            soup = bs(r.content)
            h3 = soup.find_all("h3", attrs={"class": "result-heading"})

            if self.old_data != h3:
                new_href = []
                

                for tag in h3:
                    new_href.append(tag.find("a")['href'])

                print("--------------------- Compair old & new ------------------ ")
                print("--------------------- old ------------------ ")
                print(h3)
                print("--------------------- /old ------------------ ")
                print("--------------------- new ------------------ ")
                print(self.old_data)
                print("--------------------- /new ------------------ ")
                print("--------------------- /Compair old & new ------------------ ")

                for data1 in h3:
                    if data1 not in self.old_data:
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

                    self.old_data = h3

                    driver = webdriver.Chrome(self.env.CHROME_DRIVER_PATH)

                    driver.get("https://messages.textfree.us/login")

                    time.sleep(2)
                    # username
                    username = driver.find_element_by_name("username")
                    username.send_keys(self.env.TEXT_FREE_USERNAME)

                    # password
                    password = driver.find_element_by_name("password")
                    password.send_keys(self.env.TEXT_FREE_PASS)

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
                    contactInput.send_keys(self.env.MSM_NUM)

                    #click to input message
                    emojionearea_editor = driver.find_element_by_class_name('emojionearea-editor')

                    if message_to_send != '':
                        emojionearea_editor.send_keys(f"https://sfbay.craigslist.org/search/zip?query={self.look_for}&search_distance={self.env.DISTANCE}&postal={self.env.CRAIGSLIST_ZIP} Check Craigslist {self.look_for} stuff! {message_to_send} ")
                    else:
                        emojionearea_editor.send_keys(f'Something is wrong with Craigslist {self.look_for} bot https://sfbay.craigslist.org/search/zip?query={self.look_for}&search_distance={self.env.DISTANCE}&postal={self.env.CRAIGSLIST_ZIP}')

                    #send
                    sendButton = driver.find_element_by_id('sendButton')
                    sendButton.click()

                    time.sleep(2)
                    driver.quit()
                else:
                    self.old_data = h3

            time.sleep(2)