import os
import requests
import smtplib
from bs4 import BeautifulSoup


def get_price(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    amount = soup.find("div", class_="_30jeq3 _16Jk6d").get_text()
    return amount


def send_mail(target, url=""):
    msg = f"Subject: Price dropped\n\nPlease check your desired item {url}"
    smtp = smtplib.SMTP("smtp.gmail.com", "587")
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("EMAIL", "PASSWORD")
    smtp.sendmail("EMAIL", target, msg)
    smtp.quit()


cmd = """
    PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Hurry, Price Dropped, check your mail')"
    """
if __name__ == "__main__":
    # ONLY WORKS WITH FLIPKART
    item_url = "https://shorturl.at//iDIPZ"
    compare_price = 42000
    price = get_price(item_url)
    if price < compare_price:
        send_mail("TARGET", item_url)
        os.system(f"{cmd}")
