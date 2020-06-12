from selenium import webdriver
import requests
import os
import random
import string
import json
import bs4
import time

chars = string.ascii_letters + string.digits + '!@#%^*()'
random.seed = (os.urandom(1854))

# I just looked up the top thousand baby names of 2019 for this one.
names = json.loads(open("names.json").read())

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# white hat hackers may change this url to test vulneralbility against spammers
driver.get("https://127.0.0.1/contact")

names = json.loads(open("names.json").read())
speech = json.loads(open("speech.json").read())
# just looked up the top english words spoken in the language.
words = json.loads(open("words.json").read())
emailList = ["@gmail.com","@yahoo.com", "@hotmail.com", "@outlook.com"]

def randTitle(): 
    title = ""
    for x in range(5):
        title = title + " " + random.choice(words)
    return title


for name in names:
    full_name = name + " " + random.choice(names)
    driver.find_element_by_id("Full_Name").send_keys(full_name)

    time.sleep(0.1)
    name_extra = ''.join(random.choice(string.digits))
    email = name.lower() + name_extra + random.choice(emailList)
    driver.find_element_by_id("Email_Address").send_keys(email)

    time.sleep(0.1)
    driver.find_element_by_id("Subject_Matter").send_keys(randTitle())

    time.sleep(0.1)
    driver.find_element_by_id("Your_Message").send_keys(speech)
    
    time.sleep(0.1)
    # some people have terrible security with static spam checkers. 
    driver.find_element_by_id("AntiSpam").send_keys("77")

    driver.find_element_by_xpath('//*[@type="submit"]').click()

    time.sleep(1)
    driver.get("https://127.0.0.1/contact")
    time.sleep(1)

    

    


