
#project DE
from bs4 import BeautifulSoup
import requests

url = "https://www.bseindia.com/sensex/code/16/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')

'''
url="https://www.mypetrolprice.com/10/Petrol-price-in-Ahmedabad?FuelType=0&LocationId=10"
resp=requests.get(url)

soup=BeautifulSoup(resp.text,'html.parser')
tier_prices=soup.select(".GVPrice")

stripped_tiernames=[tier.text.strip() for tier in tier_prices]

print(stripped_tiernames)
'''

table=soup.find('strong',{'id':'idcrval', 'class':'ng-binding'})
print(table)

