import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Bangalore")
# print(response.status_code)

soup= BeautifulSoup(response.content,"html.parser")
# print(soup.prettify())
cards= soup.find_all("div", attrs={"class":"mb-srp__card"})
for card in cards:
    value1=card.find("div", attrs={"class":"mb-srp__card__price--amount"})
    price=value1.text
    title= card.find("h2", attrs={"class":"mb-srp__card--title"})
    value2= card.find("div", attrs={"class":"mb-srp__card__summary--value"})
    area=value2.text
    data = "{} {} {}".format(title.text, area, price)
    print(data)
