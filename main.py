from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

what_day = input('What year would you like you travel to? Type the date in this format YYYY-MM-DD: ')

chrome_driver_path = "/Users/TaylorLoatman/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(f'https://www.billboard.com/charts/hot-100/{what_day}')

song_list = driver.find_elements(By.CSS_SELECTOR, '.chart-list li .chart-element__information__song')

for song in song_list:
    print(song.text)


driver.quit()




