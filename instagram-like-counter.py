from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
browser = webdriver.Chrome()
username = ''
password = ''
userCheck = input("whos likes u wanna count? ")
browser.get('https://www.instagram.com/')

time.sleep(2)

def searchIG(user):
    searchButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
    searchButton.click()
    time.sleep(1)
    searchField = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
    searchField.send_keys(user)
    time.sleep(1.5)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    

def loginIG(u,p):
    userfield = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    pwfield = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    login_button = browser.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div')

    userfield.send_keys(u)
    pwfield.send_keys(p)
    login_button.click()

linksList = {}

def likeScrollCount():
    picSelect = browser.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1)')
    picSelect.click()
    time.sleep(1)
    likeSelect = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button')
    likeSelect.click()
    time.sleep(0.5)
    scroller = browser.find_element_by_xpath('/html/body/div[5]/div/div[3]/div')
    ##scrollBox = browser.find_element_by_xpath('/html/body/div[5]/div/div[3]')
    browser.execute_script('arguments[0].scrollIntoView()',scroller)
    
    last_ht, ht = 0,1
    
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        ht = browser.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroller)
         
        links = scroller.find_elements_by_tag_name('a')
        for link in links:
            linksList.setdefault(link,0)
        
        ##likeList.setdefault([like.text for like in links if like.text != ''],0)
        ##print(likeList)

loginIG(username, password)
time.sleep(2)
searchIG(userCheck)
time.sleep(3)
likeScrollCount()
print(len(list(linksList.keys())))