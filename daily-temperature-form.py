import requests, webbrowser, pyperclip, random
from selenium import webdriver
import bs4
import time

delayTimeList = [60,120,180,240,300]
TimeSelected = delayTimeList[random.randint(0,4)]
print(TimeSelected)

browser = webdriver.Firefox()
browser.get('https://temptaking.ado.sg/group/2424241947e5a26be7a9c10d6720c84b')

findmember = browser.find_element_by_css_selector('#member-select > option:nth-child(3)')
findmember.click()

pinKey1 = browser.find_element_by_css_selector('#ep1')
pinKey2 = browser.find_element_by_css_selector('#ep2')
pinKey3 = browser.find_element_by_css_selector('#ep3')
pinKey4 = browser.find_element_by_css_selector('#ep4')

pinKey1.send_keys('1')
pinKey2.send_keys('2')
pinKey3.send_keys('3')
pinKey4.send_keys('4')

tempKey1 = browser.find_element_by_css_selector('#td1')
tempKey2 = browser.find_element_by_css_selector('#td2')
tempKey3 = browser.find_element_by_css_selector('#td3')

tempKey1.send_keys('3')
tempKey2.send_keys('6')
tempKey3.send_keys(str(random.randint(4,8)))

time.sleep(TimeSelected)

submitButton = browser.find_element_by_css_selector('#submit-temperature-container > button:nth-child(3)')
submitButton.click()

finalSend = browser.find_element_by_css_selector('html body.modal-open div#modal.modal.fade.show div.modal-dialog.modal-dialog-centered div.modal-content div#modal-footer.modal-footer button#submit-temp-btn.btn.btn-primary.action-btn')

finalSend.click()

browser.quit()
