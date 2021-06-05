# Scrapping Craigslist/Trash Nothing!
Free Apple products & more through scrapping Craigslist/Trash Nothing! These python files use bs4 & selenium to scrape the web & send you a text message when you find that awesome thing your looking for! The file are setup to for searching for free apple products, computers, laptops, & video games. 

***The story behind this build***
My Friend was telling me how he got a free Mac Book Air from Craigslist! I was like wow, & I started looking at Craigslist through out the day. But I was not finding anything, although my friend keep finding tons of free apple product one he sold for over $2K! So I build a web scraper & the rest is history!

## Tech Used
- Python
- Bs4
- Selenium
- requests
- dotenv


## Setup, Install & Run

1. `pip3 install -r requirements.txt`
2. Creat a free account on [TextFree.us](https://messages.textfree.us/login)
3. [Download Chrome Driver](https://sites.google.com/achromium.org/chromedriver/downloads)
    - NOTE: You have Google Chrome & the Chrome Driver must be the same vertion
    - FIND VERTION: 
        - Open Google Chrome
        - click 3 dots in upper right corner,
        - click `Help`
        - click `About Google Chrome`
4. `mv env.example .env`
5. Setup .env
    - Text Free Username & Password  
    ```
    TEXT_FREE_USERNAME=UserName
    TEXT_FREE_PASS=Password
    ```
    - phone number you can be texted at
    `MSM_NUM=5555555555`
    - your zip code
    `CRAIGSLIST_ZIP=55555`
    - find & copy the path where you saved chromedriver
    `CHROME_DRIVER_PATH=/some/path/to/chromedriver`
    - search your zip code on trashnothing.com & copy the radiaous in the URL
    `TRASH_NOTHING_RADIAOUS=555555`
6. choice file to run
    - `python3 apple_craigslitst_scrape.py`
    - `python3 apple_trash_nothing.py`
    - `python3 computer_craigslit.py`
    - `python3 computer_trash_nothing.py`
    - `python3 laptop_craigslit.py`
    - `python3 laptop_trash_nothing.py`
    - `python3 mac_craiglist.py`
    - `python3 mac_trash_nothing.py`
    - `python3 video_game_craigslist.py`
    - `python3 video_game_trash_nothing.py`


## IMG

***Enter command***

![Image of the terminal just before entering the command to run the scraper](https://raw.githubusercontent.com/LWRGitHub/cs_scraper/master/img/start.png?token=AMXINNFFM44HHAV45RJVNVTAYVAUQ)


***Runing***

![Image of the terminal runing the web scraper](https://raw.githubusercontent.com/LWRGitHub/cs_scraper/master/img/runing.png?token=AMXINND6VGLJDAPMDFQO7QTAYVASE)


***App sending you a Text***

![Image of the app having found something & starting to text a number.](https://raw.githubusercontent.com/LWRGitHub/cs_scraper/master/img/text.png?token=AMXINNDJRDIDFVY7K4SOCJTAYVAWO)