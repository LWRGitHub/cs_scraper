from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from Env import Env


class Trno_scrp:
    
    def __init__(self, look_for):
        # dotenv
        self.env = Env()
        self.look_for = look_for.lower()

        # bs4
        # set old data
        self.r = requests.get(f"https://trashnothing.com/beta/browse?radius={self.env.RADIAOUS}&search={self.look_for}")
        self.soup = bs(self.r.content)
        self.old_data = self.soup.find_all("a", attrs={"class": "offer"})
    

    def indefinite_scrp(self):
        # uncomment `old_data` to recive all items when you first run the app
        self.old_data = []

        all_href = []
        for a in self.old_data:
            all_href.append(a['href'])
        print(all_href)

        while True:
            # get new data
            r = requests.get(f"https://trashnothing.com/beta/browse?radius={self.env.RADIAOUS}&search={self.look_for}")
            soup = bs(r.content)
            recent_data = soup.find_all("a", attrs={"class": "offer"})

            if self.old_data != recent_data:
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
                print(self.old_data)
                print("--------------------- /new ------------------ ")
                print("--------------------- /Compair old & new ------------------ ")
                
                there_is_a_new_href = False

                message_to_send = ''
                for data_href in new_href:
                    if data_href not in all_href:
                        there_is_a_new_href = True
                        message_to_send += f"https://trashnothing.com{data_href} "
                        all_href.append(data_href)

                
                if there_is_a_new_href:
                    
                    print("----------------message----------------")
                    print(message_to_send)
                    print("----------------/message----------------")

                    self.old_data = recent_data

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
                        emojionearea_editor.send_keys(f"https://trashnothing.com/beta/browse?radius={self.env.RADIAOUS}&search={self.look_for} Check Trash Nothing {self.look_for} stuff! {message_to_send} ")
                    else:
                        emojionearea_editor.send_keys(f'Something is wrong with Trash Nothing {self.look_for} bot https://trashnothing.com/beta/browse?radius={self.env.RADIAOUS}&search={self.look_for}')

                    #send
                    sendButton = driver.find_element_by_id('sendButton')
                    sendButton.click()

                    time.sleep(2)
                    driver.quit()
                else:
                    self.old_data = recent_data

            time.sleep(2)