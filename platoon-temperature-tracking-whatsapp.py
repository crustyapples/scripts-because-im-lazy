import pyautogui
import pyperclip
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://temptaking.ado.sg/overview/c2c1b6e48175a009d6e403af4b336773')
time.sleep(10)

pyautogui.hotkey('ctrl', 'a')
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

TemperatureData = pyperclip.paste()

time.sleep(1)
browser.quit()

excludeList = ['A4101', 'A4108', 'A4114', 'A4115', 'A4116', 'A4208', 'A4211', 'A4212', 'A4214', 'A4215',
               'A4216', 'A4313', 'A4314', 'A4315', 'A4316', 'A4401', 'A4403', 'A4409', 'A4410', 'A4414', 'A4415',
               'A4416']

DoneAMRegex = re.compile(r"(A4[1-9][0-9]{2})\t(\S{6})\t(\w{3}|\S{6})")
DonePMRegex = re.compile(r"(A4[1-9][0-9]{2})\t\S{6}\t(\S{6})")
NotDoneRegex = re.compile(r"(A4[1-9][0-9]{2})\t(\w{3})\t(\w{3})")

AMmessageList = []
PMmessageList = []
NotDoneMessageList = []

DoneAMList = DoneAMRegex.findall(TemperatureData)
DonePMList = DonePMRegex.findall(TemperatureData)
NotDoneList = NotDoneRegex.findall(TemperatureData)

for i in range(len(NotDoneList)):
    NotDoneMessageList.append(NotDoneList[i][0])
for i in range(len(DonePMList)):
    PMmessageList.append(DonePMList[i][0] + ' PM: ' + DonePMList[i][1])
for i in range(len(DoneAMList)):
    AMmessageList.append(DoneAMList[i][0] + ' AM: ' + DoneAMList[i][1])
for i in excludeList:
    if i in NotDoneMessageList:
        NotDoneMessageList.remove(i)

AMcount = str(len(DoneAMList))
PMcount = str(len(DonePMList))
NotDoneCount = str(len(NotDoneMessageList))

AMmessage = ' '.join(AMmessageList)
NotDoneMessage = ', '.join(NotDoneMessageList)
PMmessage = ' '.join(PMmessageList)

FinalMessage = '*Platoon 4 Daily Temperature Reporting* \n' + '*AM Session:* ' + AMcount + '\n' + AMmessage + '\n *PM ' \
                                                                                                          'Session:* '\
               + PMcount + '\n' + PMmessage + ' \n *Not Done AT ALL:* ' + NotDoneCount + '\n' + NotDoneMessage

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=selenium")
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
driver.get('https://web.whatsapp.com')

name = 'Platoon#4'
msg = FinalMessage
time.sleep(30)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

textbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
print(textbox)

textbox.send_keys(msg)
time.sleep(3)
textbox.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
