import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

f = open("coins.csv", "w", encoding="utf-8-sig", newline="\n")
file = csv.writer(f)
# Market Cap = Current Price x Circulating Supply.
file.writerow(["Name", "Price", "Market Cap", "Circulating Supply"])
h = {"Accept-Language": "en-US"}

pg = 1

while pg < 6:
    url = "https://coinmarketcap.com/?page=" + str(pg)
    r = requests.get(url, headers=h)

    soup = BeautifulSoup(r.text, "html.parser")
    soup2 = soup.find("table", {"class": "h7vnx2-2"}).tbody
    coins = soup2.find_all("tr")

    for c in coins:

        if not c.has_attr("class"):
            name = c.find("p", {"class": "sc-1eb5slv-0 iworPT"}).text
            price = c.find("div", {"class": "sc-131di3y-0 cLgOOr"}).a.span.text.replace("$", "")
            market_cap = c.find("span", {"class": "sc-1ow4cwt-1 ieFnWP"}).text.replace("$", "")
            market_cap = int(market_cap.replace(",", ""))
            circulating_supply = c.find("p", {"class": "sc-1eb5slv-0 kZlTnE"}).text
            file.writerow([name, price, market_cap, circulating_supply])
    pg += 1
    sleep(5)
