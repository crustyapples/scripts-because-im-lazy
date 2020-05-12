from __future__ import unicode_literals
from selenium import webdriver
from pytube import YouTube
import moviepy.editor as mp
import os
import re

ingredient = input("mukbang ingredient: ")
browser = webdriver.Chrome()
url = f'https://www.youtube.com/results?search_query=no+talking+mukbang+{ingredient}'
browser.get(url)
firstMukbang = browser.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
firstMukbang.click()
URLlist = browser.current_url
browser.quit()
print(URLlist)
target_folder = os.getcwd()
y = YouTube(URLlist)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path=target_folder)

for file in [n for n in os.listdir(target_folder) if re.search('mp4',n)]:
    full_path = os.path.join(target_folder, file)
    output_path = os.path.join(target_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path).subclip(10,) # disable if do not want any clipping
    clip.write_audiofile(output_path)
