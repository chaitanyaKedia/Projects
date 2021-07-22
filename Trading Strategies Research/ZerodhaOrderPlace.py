import requests
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xlrd import open_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
def zerodha_login():
    USERID=""
    Password=""
    Pin=""
    browser.get('https://kite.zerodha.com/chart/web/ciq/NSE/INFRATEL/7458561')
    user=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/input')
    passw=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/input')
    user.send_keys(USERID)
    passw.send_keys(Password)
    login=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button')
    login.click()
    time.sleep(1)
    PIN=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/div/input')
    PIN.send_keys(Pin)
    Continue=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/button')
    Continue.click()

def check_funds():
    Funds=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/a[5]/span')
    Funds.click()
    time.sleep(2)
    cash_avail=float(browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/h1').text)
    return cash_avail

def buy():
    MIS=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[1]/div[1]/div/div[1]/label')
    MIS.click()
    Q=5
    Qty=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[2]/div[1]/div/input')
    Qty.send_keys(Q)
    time.sleep(0.1)
    MarginCalc=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[3]/span[3]/span')
    MarginCalc.click()
    time.sleep(0.2)
    MarginReq=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[3]/span[2]').text
    MarginReq=float(MarginReq[1:])
    Limit=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[1]/div[2]/div/div[2]')
    Limit.click()
    Price=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[2]/div[2]/div/input')
    Buy=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[3]/div[2]/button[1]')
    Buy.click()

def sell():
    MIS=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[1]/div[1]/div/div[1]/label')
    MIS.click()
    Q=5
    Qty=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[2]/div[1]/div/input')
    Qty.send_keys(Q)
    time.sleep(0.1)
    MarginCalc=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[3]/span[3]/span')
    MarginCalc.click()
    time.sleep(0.2)
    MarginReq=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[3]/span[2]').text
    MarginReq=float(MarginReq[1:])
    stoploss_market=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[1]/div[2]/div/div[4]')
    stoploss_market.click()
    Price=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[2]/div[2]/div/input')
    Buy=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[4]/div[3]/div[2]/button[1]')
    Buy.click()

def check_market_depth():
    mkt_depth=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/button[3]')
    mkt_depth.click()
    time.sleep(2)
    bid_tot=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/table[1]/tfoot/tr/td[2]')
    off_tot=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/table[2]/tfoot/tr/td[2]')
    bid=bid_tot.text.split(",")
    offer=off_tot.text.split(",")
    bid_total=int(''.join(bid))
    offer_total=int(''.join(offer))
    ratio=round(bid_total/offer_total,4)
    return ratio

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
browser = webdriver.Chrome(options=option)

zerodha_login()

time.sleep(2)

cash=check_funds()

section3=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[3]')
section3.click()

#ticker=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/span[1]/span/span')
#ticker.click()
#buy_button=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/button[1]')
#buy_button.click()
#buy()

#ticker=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/span[1]/span/span')
#ticker.click()
#sell_button=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/button[2]')
#sell_button.click()
#sell()

ticker=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/span[1]/span/span')
ticker.click()
mkt_depth=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/button[3]')
mkt_depth.click()
time.sleep(2)
bid_tot=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/table[1]/tfoot/tr/td[2]')
off_tot=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/table[2]/tfoot/tr/td[2]')
arr=[]
while(True):
    bid=bid_tot.text.split(",")
    offer=off_tot.text.split(",")
    bid_total=int(''.join(bid))
    offer_total=int(''.join(offer))
    ratio=round(bid_total/offer_total,4)
    arr.append(ratio)
    print(ratio)
    time.sleep(0.7)

