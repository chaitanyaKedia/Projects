from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from tkinter import *

def zerodha_login():
    file=open(r'G:\credentials.txt','r')
    det=file.read().split('\n')
    USERID=det[0]
    Password=det[1]
    Pin=det[2]
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

def load_stock():
    search=tick.get()
    Label(text=search).grid(row=2,column=0)
    buy=Button(root,text="buy")
    sell=Button(root,text="sell")
    buy.grid(row=2, column=4)
    sell.grid(row=2,column=5)
    Label(text="qty").grid(row=1, column=6)
    qty=Entry(root)
    qty.grid(row=2,column=6)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/input').send_keys(search)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/ul/div/li[1]/span[1]/span').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span[1]/span/span').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/span/span[3]').click()
    time.sleep(2)
    update()
    
    
def update():
    bid=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/table[1]/tbody/tr[1]/td[1]').text
    offer=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/table[2]/tbody/tr[1]/td[1]').text
    ltp=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/span[2]/span[3]').text

    #Label for Bid price
    Label(text=bid).grid(row=2,column=1)

    #Label for Offer Price
    Label(text=offer).grid(row=2,column=2)

    #Label for LTP
    Label(text=ltp).grid(row=2,column=3)

    
    
    root.after(10,update)


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome()

zerodha_login()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[3]').click()

root=Tk()

Label(text="Enter the ticker Symbol").grid(row=0,column=0)
#Entry box for entering the symbol
tick=Entry(root)
tick.grid(row=0,column=1)

#Go button to search the stock and load the data

go=Button(root,text="GO",command=load_stock)
go.grid(row=0,column=2)

#Label for Ticker
Label(text="Ticker").grid(row=1,column=0)
#Label for Bid price
Label(text="BID").grid(row=1,column=1)
#Label for Offer Price
Label(text="OFFER").grid(row=1,column=2)
#Label for LTP
Label(text="LTP").grid(row=1,column=3)

root.mainloop()
