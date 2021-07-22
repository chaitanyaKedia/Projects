from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xlrd import open_workbook
from selenium.webdriver.common.keys import Keys
# Enter the credentials
usernameStr = 
passwordStr =
# Enter the amount
amt=
book = open_workbook('zzz.xlsx')
sheet = book.sheet_by_index(0)
keys = sheet.col_values(0)
browser = webdriver.Chrome()
browser.get(('https://evd.tatasky.com/EVD_WEB/'))
username = browser.find_element_by_xpath('/html/body/form/center/center/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input')
username.send_keys(usernameStr)
password = browser.find_element_by_xpath('/html/body/form/center/center/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input')
password.send_keys(passwordStr)
login_box = browser.find_element_by_xpath('/html/body/form/center/center/table/tbody/tr/td[2]/table/tbody/tr[5]/td/center/input[1]') 
login_box.click()
browser.implicitly_wait(3)
#browser.switch_to_alert().accept()
browser.get('https://evd.tatasky.com/EVD_WEB/TestAction.evd?goto=recharge')
for i in range(0,1500):
    user=str(int(keys[i]))
    usname=browser.find_element_by_xpath('//*[@id="dst_mdn"]')
    amount=browser.find_element_by_xpath('/html/body/form/center/table/tbody/tr[14]/td[2]/input[1]')
    submit=browser.find_element_by_xpath('/html/body/form/center/table/tbody/tr[15]/td[1]/input')
    usname.send_keys(user)
    amount.send_keys(amt)  
    submit.click()
    browser.get('https://evd.tatasky.com/EVD_WEB/TestAction.evd?goto=recharge')
{"mode":"full","isActive":false}
