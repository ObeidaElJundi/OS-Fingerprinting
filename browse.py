# This script will automate browing the internet for the sake of collecting packets to train OS fingerprinting model
# coded by: Obeida ElJundi (aka: coding4fun)

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


def scroll(driver, fast_scroll=True):
    html = driver.find_element_by_tag_name('html')
    for i in range(100):
        html.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.1 if fast_scroll else 0.5)

def Twitter(driver):
    # navigate to Google images
    driver.get('https://twitter.com/goodfellow_ian?lang=en')
    # scroll down to load more images and get more packets
    scroll(driver, fast_scroll=True)

def Google(driver):
    # navigate to Google images
    driver.get('https://www.google.com.lb/imghp')
    # search for 'nature wallpaper hd'
    search = driver.find_element_by_name('q')
    search.clear()
    search.send_keys('nature wallpaper hd')
    search.send_keys(Keys.RETURN)
    # scroll down to load more images and get more packets
    #scroll(driver, fast_scroll=False)
    html = driver.find_element_by_tag_name('html')
    for i in range(100):
        html.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        try:
            show_more_button = driver.find_element_by_id('smb')
            if show_more_button: show_more_button.click()
        except:
            pass

def Youtube(driver):
    # navigate to Youtube
    driver.get('https://www.youtube.com/watch?v=bMr7vaJJXGI') # 4 mins & 23 seconds
    # sleep 5 mins till the end of the video
    time.sleep(5*60)

def Reddit(driver):
    # navigate to Reddit (machine learning subreddit)
    driver.get('https://www.reddit.com/r/machinelearning') # 4 mins & 23 seconds
    # scroll down to load more images and get more packets
    scroll(driver, fast_scroll=True)

def Instagram(driver):
    # navigate to Instagram (AUB page)
    driver.get('https://www.instagram.com/aub_lebanon/?hl=en')
    # scroll down to load more images and get more packets
    scroll(driver, fast_scroll=True)

def main():
    if len(sys.argv) != 3:
        print('ERROR! Three arguments should be provided!')
        print('Usage: python3 browse.py <driver_executable_path> <train|test>')
        print('Example: python3 browse.py /home/user/chromedriver train')
        sys.exit(1)

    driver_executable_path = sys.argv[1]
    mode = sys.argv[2]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito') # open incognito instead of normal chrome
    chrome_options.add_argument('start-maximized') # full screen
#    chrome_options.add_argument('--disable-extensions')
#    chrome_options.add_argument('disable-infobars')
#    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--no-zygote')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # get an instance of Chrome WebDriver
    driver = webdriver.Chrome(executable_path=driver_executable_path, options=chrome_options) # executable_path=

    print('Chrome started!')

    if mode == 'train':
        Twitter(driver)
        print('Twitter Done!')
        Google(driver)
        print('Google Done!')
        Youtube(driver)
        print('Youtube Done!')
    else:
        Reddit(driver)
        print('Reddit Done!')
        Instagram(driver)
        print('Instagram Done!')

    driver.close()
    print('DONE :)')


if __name__ == '__main__':
    main()
