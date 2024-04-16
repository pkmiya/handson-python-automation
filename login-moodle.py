from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os
from dotenv import load_dotenv

load_dotenv()

login_url = os.environ.get("LOGIN_URL")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

driver = webdriver.Chrome()
driver.get(login_url)
time.sleep(1)

# ユーザー名⼊⼒
name_box = driver.find_element(By.ID, "username")
name_box.send_keys(username)

# パスワードを⼊⼒
pass_box = driver.find_element(By.ID, "password")
pass_box.send_keys(password)

# ログインボタンをクリック
login_btn = driver.find_element(By.ID, "loginbtn")
login_btn.click()
if input("Enterを押すと終了します。"):
    driver.quit()
