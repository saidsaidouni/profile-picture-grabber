from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import os, shutil
from PIL import Image 

op = webdriver.ChromeOptions()
op.add_argument('headless')

#variables---------------------------------------------------------------------------------------------------
username = input("please enter the username of the user: ")
username_png = input("enter how do you want the name of the image to be: ")
#---------------------------------------------------------------------------------------------------

said = "./chromedriver.exe"
# driver = webdriver.Chrome(said)
driver = webdriver.Chrome(said, options=op)
driver.get(f"https://www.instadp.com/profile/{username}")

# we press on full size icon
print(f"""
                *************************************************
                ****finding the profile picture of '{username}'****
                *************************************************
""")
sleep(3)
full_size = driver.find_element_by_xpath("/html/body/article/div[2]/ul/li[2]/a/i")
full_size.click()
print("""
                ***************
                ****found! ****
                ***************
""")

#get the picture
sleep(3)
print("downloading...")
picture = driver.find_element_by_xpath("/html/body/article/div[2]/section[2]/div[4]/a[1]/img")
src = picture.get_attribute('src')

# download the image
urllib.request.urlretrieve(src, f"./users/mynam/Desktop/{username_png}.png")
print("successfully downloaded! ")
print("picture been downloaded in the same path of this program")

