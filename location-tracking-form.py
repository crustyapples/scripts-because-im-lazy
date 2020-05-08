from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import pyautogui

sectionThreeDict = {4301:'L L Yi', 4302:'L Z Ting', 4303: 'J J Teo', 4304: 'MD Fathur', 4305: 'N Abraham', 4306:'K K Lechemanam', 4307: 'Z W Ng', 4308: 'R V Raj', 4309:'N B Nahar', 4310: 'Z C Rodrigues', 4311: 'O N Dave', 4312: 'D Carlos',4201:'Gandhi',4202:'Wang X D', 4203:'Cao Z J',4204:'Nyam W L',4205:'Shan W K',4206:'Phang J Y',4207: 'Ang Z J', 4209: 'Lim K H',4210:'Gan W H',4213: 'Pramit'} 
Time = input("What time is it? (24hr format): ")
ClockTime = int(Time)
for num in sectionThreeDict.keys():
    browser = webdriver.Chrome()
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeNXaCyQkG6TO3ycrSnRTANkSDVde0fJrq0cV42eSMzHTHojg/viewform')
    time.sleep(1.5)
    fourDnumber = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
    Initials = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
    TimeCalled = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div.freebirdFormviewerViewItemsTextItemWrapper > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
    OpenNum = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(4) > div > div.quantumWizMenuPaperselectEl.appsMaterialWizMenuPaperselectSelect.freebirdFormviewerViewItemsSelectSelect.freebirdThemedSelectDarkerDisabled.noMaxWidth > div:nth-child(1) > div.quantumWizMenuPaperselectOptionList > div.quantumWizMenuPaperselectOption.appsMaterialWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isPlaceholder.isSelected > span')
    MethodContact = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(5) > div > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    CheckBox1 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[1]/div/label/div/div[1]/div[2]')
    CheckBox2 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div/label/div/div[1]/div[2]')
    CheckBox3 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[3]/div/label/div/div[1]/div[2]')
    CheckBox4 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[4]/div/label/div/div[1]/div[2]')
    CurrentLocation = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(7) > div > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    Remarks = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(8) > div > div.quantumWizTextinputPapertextareaEl.modeLight.freebirdFormviewerViewItemsTextLongText.freebirdThemedInput > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
    Submit = browser.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span > span')
    fourDnumber.send_keys(num)
    Initials.send_keys(sectionThreeDict.get(num))
    RandAdd = random.randint(1,2)
    ClockTime += RandAdd
    print(ClockTime)
    TimeCalled.send_keys(ClockTime)
    OpenNum.click()
    time.sleep(1)
    pyautogui.press('1')
    pyautogui.press('enter')
    MethodContact.click()
    CheckBox1.click()
    CheckBox2.click()
    CheckBox3.click()
    CheckBox4.click()
    CurrentLocation.click()
    Remarks.send_keys('NIL')
    Submit.click()
    time.sleep(1)
    browser.quit()
