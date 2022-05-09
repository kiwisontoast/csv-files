from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from PIL import ImageGrab

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://play2048.co")
driver.maximize_window()
body=driver.find_element_by_css_selector('body')
pixelMeasurex=[616,727,778,900,616,727,778,900,616,727,778,900,576,676,776,900]
pixelMeasurey=[408,420,420,420,550,550,550,550,650,650,650,650,723,723.723,723]

while True:    
    body.send_keys(Keys.RIGHT)
    body.send_keys(Keys.DOWN)
    rgbtotal=0
    
    load=ImageGrab.grab().load()
    for i in range (1,16):
        rgbtotal+=load[pixelMeasurex[i]],[pixelMeasurey[i]]
        compare=rgbtotal
    if(compare==rgbtotal):{
        body.send_keys(Keys.LEFT)
    }
       
    #best 7800  
