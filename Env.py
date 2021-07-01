from dotenv import load_dotenv
import os

load_dotenv()

class Env:

    def __init__(self):
        self.TEXT_FREE_USERNAME = os.getenv('TEXT_FREE_USERNAME')
        self.TEXT_FREE_PASS = os.getenv('TEXT_FREE_PASS')
        self.MSM_NUM = os.getenv('MSM_NUM')
        self.CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
        self.CRAIGSLIST_ZIP = os.getenv('CRAIGSLIST_ZIP')
        self.RADIAOUS = os.getenv('TRASH_NOTHING_RADIAOUS')
        self.DISTANCE = os.getenv('CRAIGSLIST_DISTANCE')
