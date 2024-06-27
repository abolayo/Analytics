import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
my_email = "arduinoafrica@gmail.com"
password = "get_password" # from the sender email security settings

url = ('https://www.amazon.ca/Swimsuit-Islamic-Swimwear-Burkini-Protection/dp/B0B2DK1MFM/ref=sr_1_1_sspa?crid'
       '=3O7SU1L5C5AZ9&dib=eyJ2IjoiMSJ9.JlsbmgZQwJFU0CZZvVJ10S5GABQvlm-bEPe1VnsOjLYujE5hYBVFBkJWGrCT_PpIdvautGi'
       '-SOfD5EHgCW-gsSkl'
       '-CGrvZmmsTez34GEgXmnrSyVy3ig_WC0UG5sUu0xnAAfnU7ifrG27PHba6UzKT7EaGf0jVEDH74LusDrO29FY_0HVUbLNm06i2o5ugR4EOsIgNX-u3r7Urv9aYEFamfGWxReITRd3-h0OiPC5hgkgZ8gYHxuOePNVVBOZjWgExytxwFOjkWFZCmrC8sEDYW2eoex28dYjJZUuL1jj3s.RbwtO2tXJ24deroc8SQ2bB4kW-iDfGlZd8ESQPZiXK8&dib_tag=se&keywords=women%2Bislamic%2Bswim%2Bsuit&qid=1719505527&sprefix=wemon%2Bislamic%2Bswim%2Bsuit%2Caps%2C86&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1')
headers = {'Accept-Language': 'en-US,en;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/126.0.0.0 Safari/537.36'}
Data = requests.get(url, headers=headers)
response = Data.text
soup = BeautifulSoup(response, 'html.parser')
price = soup.find("div", class_="a-section a-spacing-none aok-align-center aok-relative").getText()
current_price = float(price.split()[0][1:])
title = soup.find('span', class_='a-size-large product-title-word-break').getText().strip()
product_link = url
set_value = 35.0

# print(f"Subject:Hello\n{title}\n{current_price}\n{product_link}")
if current_price <= set_value:
    with smtplib.SMPT("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, passwd=password)
        connection.sendmail(to_addrs="somebody@yahoo.com",
                            from_addr=my_email,
                            msg=f"Subject:Hello\n{title}\n{current_price}\n{product_link}"
                            )
