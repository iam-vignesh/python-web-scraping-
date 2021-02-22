import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_2_sspa?dchild=1&keywords=iphone+11+pro&qid=1595561443&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVNzBOTUJFWTBXTk4mZW5jcnlwdGVkSWQ9QTA3NTg1OTE0WERBTlRFTlc1NzEmZW5jcnlwdGVkQWRJZD1BMDI3NDY0MThHVUg0SzAxMDVDRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def iphone_price():
    page = requests.get(URL,headers=headers)
    print(page)
    if page.status_code == 200:
        print("Connection Established")

    site = BeautifulSoup(page.content, 'html.parser')

    product = site.find(id ="productTitle").get_text()
    price = site.find(id ="priceblock_ourprice").get_text()
    print(product.strip())
    print("Actual Price is")
    print(price)
    real_price = price[2:10]
    print(real_price)
    floated_price = float(real_price.replace(',',''))
    print("Rounded off Price is")
    print(floated_price)

    if(floated_price < 500000.00):
        trigger_mail()

def trigger_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo
    server.starttls()
    server.ehlo
    server.login("email","password")

    sub = "THERE IS A PRICE DROP"
    body = "Check it out: https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_2_sspa?dchild=1&keywords=iphone+11+pro&qid=1595561443&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVNzBOTUJFWTBXTk4mZW5jcnlwdGVkSWQ9QTA3NTg1OTE0WERBTlRFTlc1NzEmZW5jcnlwdGVkQWRJZD1BMDI3NDY0MThHVUg0SzAxMDVDRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

    email = f"{sub}\n\n\n{body}"

    server.sendmail(
        "from email address",
        "to email address",
        email
    )
    print("This looks within your budget!\n")
    print("SENT EMAIL WITH THE LINK TO BUY...")
    server.quit

while(True):
    iphone_price()
    time.sleep(10800)











