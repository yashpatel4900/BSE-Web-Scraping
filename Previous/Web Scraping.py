# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:26:25 2020

@author: india
"""
'''
import requests 
from bs4 import BeautifulSoup

url="https://www.mypetrolprice.com/10/Petrol-price-in-Ahmedabad?FuelType=0&LocationId=10"
resp=requests.get(url)

soup=BeautifulSoup(resp.text,'html.parser')
tier_prices=soup.select(".GVPrice")

stripped_tiernames=[float(tier.text.strip()) for tier in tier_prices]

print(stripped_tiernames)
'''

#project DE

from bs4 import BeautifulSoup
import requests

url = "https://www.bseindia.com/sensex/code/16/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')
'''
print(soup.title.text)
for link in soup.find_all('a'):
    print(link.get('title'))
    print(link.get('href'))
table = soup.find('table',attrs = {"class":"svboxgreen"})
table_data = table.tbody.find_all("tr")

headings = []
for td in table_data[0].find_all("td"):
    headings.append(td.b.text.replace('\n', ' ').strip())
    
print(headings)


<div class="heatamaparea largetable" ng-show="loader.HMloaded">
                        <div id="mainDiv" style="width: 100%; height: 100%; float:right;"><table border="0" width="100%" height="100%" style="font-size:11px;color:black;" cellpadding="0" cellspacing="2" align="center"><tbody><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,29)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;INFY</td></tr><tr><td>795.25</td></tr><tr><td style="padding-top:3px;">-0.18 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,28)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;KOTAKBANK</td></tr><tr><td>1678.35</td></tr><tr><td style="padding-top:3px;">-0.50 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,27)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HDFCBANK</td></tr><tr><td>1210.00</td></tr><tr><td style="padding-top:3px;">-0.60 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,26)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ULTRACEMCO</td></tr><tr><td>4397.20</td></tr><tr><td style="padding-top:3px;">-0.77 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,25)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;INDUSINDBK</td></tr><tr><td>1170.55</td></tr><tr><td style="padding-top:3px;">-0.95 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,24)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TECHM</td></tr><tr><td>820.15</td></tr><tr><td style="padding-top:3px;">-1.13 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,23)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;NESTLEIND</td></tr><tr><td>16340.10</td></tr><tr><td style="padding-top:3px;">-1.23 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,22)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ASIANPAINT</td></tr><tr><td>1818.75</td></tr><tr><td style="padding-top:3px;">-1.31 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,21)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HINDUNILVR</td></tr><tr><td>2216.00</td></tr><tr><td style="padding-top:3px;">-1.42 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,20)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;SBIN</td></tr><tr><td>322.90</td></tr><tr><td style="padding-top:3px;">-1.45 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,19)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;POWERGRID</td></tr><tr><td>186.55</td></tr><tr><td style="padding-top:3px;">-1.48 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,18)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;NTPC</td></tr><tr><td>109.75</td></tr><tr><td style="padding-top:3px;">-1.48 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,17)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BAJFINANCE</td></tr><tr><td>4803.35</td></tr><tr><td style="padding-top:3px;">-1.58 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,16)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;LT</td></tr><tr><td>1259.55</td></tr><tr><td style="padding-top:3px;">-1.66 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,15)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;SUNPHARMA</td></tr><tr><td>398.05</td></tr><tr><td style="padding-top:3px;">-1.69 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,14)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TCS</td></tr><tr><td>2116.30</td></tr><tr><td style="padding-top:3px;">-1.86 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,13)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ITC</td></tr><tr><td>203.00</td></tr><tr><td style="padding-top:3px;">-2.12 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,12)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HCLTECH</td></tr><tr><td>595.15</td></tr><tr><td style="padding-top:3px;">-2.14 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,11)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;M&amp;M</td></tr><tr><td>513.05</td></tr><tr><td style="padding-top:3px;">-2.23 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,10)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;AXISBANK</td></tr><tr><td>725.80</td></tr><tr><td style="padding-top:3px;">-2.44 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,9)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HEROMOTOCO</td></tr><tr><td>2183.85</td></tr><tr><td style="padding-top:3px;">-2.51 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,8)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;RELIANCE</td></tr><tr><td>1444.85</td></tr><tr><td style="padding-top:3px;">-2.74 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,7)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BAJAJ-AUTO</td></tr><tr><td>2980.10</td></tr><tr><td style="padding-top:3px;">-2.75 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,6)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BHARTIARTL</td></tr><tr><td>529.80</td></tr><tr><td style="padding-top:3px;">-2.88 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,5)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ICICIBANK</td></tr><tr><td>529.55</td></tr><tr><td style="padding-top:3px;">-3.13 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,4)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TITAN</td></tr><tr><td>1279.80</td></tr><tr><td style="padding-top:3px;">-3.24 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,3)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HDFC</td></tr><tr><td>2292.85</td></tr><tr><td style="padding-top:3px;">-3.29 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,2)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;MARUTI</td></tr><tr><td>6468.20</td></tr><tr><td style="padding-top:3px;">-4.24 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,1)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ONGC</td></tr><tr><td>98.00</td></tr><tr><td style="padding-top:3px;">-4.72 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv(event,this,0)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TATASTEEL</td></tr><tr><td>415.35</td></tr><tr><td style="padding-top:3px;">-6.39 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;color:blue"><td colspan="6" align="left" height="20px" valign="middle"><table width="100%"><tbody><tr><td align="left" valign="middle"></td><td style="font-size:13px; font-weight:normal; color:white;" align="right"><div class="text-left"><input type="button" value="Alphabetical View" class="btn btn-default" onclick="javascript:DivSwitch(1);"></div></td></tr></tbody></table></td></tr></tbody></table></div>
                        <div id="mainDiv1" style="width: 100%; height: 100%; float:right;display:none"><table border="0" width="100%" height="100%" style="font-size:11px;color:black;" cellpadding="0" cellspacing="2" align="center"><tbody><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,0)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ASIANPAINT</td></tr><tr><td>1818.75</td></tr><tr><td style="padding-top:3px;">-1.31 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,1)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;AXISBANK</td></tr><tr><td>725.80</td></tr><tr><td style="padding-top:3px;">-2.44 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,2)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BAJAJ-AUTO</td></tr><tr><td>2980.10</td></tr><tr><td style="padding-top:3px;">-2.75 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,3)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BAJFINANCE</td></tr><tr><td>4803.35</td></tr><tr><td style="padding-top:3px;">-1.58 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,4)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;BHARTIARTL</td></tr><tr><td>529.80</td></tr><tr><td style="padding-top:3px;">-2.88 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,5)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HCLTECH</td></tr><tr><td>595.15</td></tr><tr><td style="padding-top:3px;">-2.14 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,6)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HDFC</td></tr><tr><td>2292.85</td></tr><tr><td style="padding-top:3px;">-3.29 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,7)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HDFCBANK</td></tr><tr><td>1210.00</td></tr><tr><td style="padding-top:3px;">-0.60 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,8)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HEROMOTOCO</td></tr><tr><td>2183.85</td></tr><tr><td style="padding-top:3px;">-2.51 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,9)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;HINDUNILVR</td></tr><tr><td>2216.00</td></tr><tr><td style="padding-top:3px;">-1.42 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,10)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ICICIBANK</td></tr><tr><td>529.55</td></tr><tr><td style="padding-top:3px;">-3.13 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,11)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;INDUSINDBK</td></tr><tr><td>1170.55</td></tr><tr><td style="padding-top:3px;">-0.95 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,12)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;INFY</td></tr><tr><td>795.25</td></tr><tr><td style="padding-top:3px;">-0.18 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,13)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ITC</td></tr><tr><td>203.00</td></tr><tr><td style="padding-top:3px;">-2.12 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,14)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;KOTAKBANK</td></tr><tr><td>1678.35</td></tr><tr><td style="padding-top:3px;">-0.50 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,15)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;LT</td></tr><tr><td>1259.55</td></tr><tr><td style="padding-top:3px;">-1.66 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,16)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;M&amp;M</td></tr><tr><td>513.05</td></tr><tr><td style="padding-top:3px;">-2.23 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,17)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;MARUTI</td></tr><tr><td>6468.20</td></tr><tr><td style="padding-top:3px;">-4.24 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,18)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;NESTLEIND</td></tr><tr><td>16340.10</td></tr><tr><td style="padding-top:3px;">-1.23 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,19)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;NTPC</td></tr><tr><td>109.75</td></tr><tr><td style="padding-top:3px;">-1.48 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,20)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ONGC</td></tr><tr><td>98.00</td></tr><tr><td style="padding-top:3px;">-4.72 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,21)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;POWERGRID</td></tr><tr><td>186.55</td></tr><tr><td style="padding-top:3px;">-1.48 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,22)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;RELIANCE</td></tr><tr><td>1444.85</td></tr><tr><td style="padding-top:3px;">-2.74 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,23)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;SBIN</td></tr><tr><td>322.90</td></tr><tr><td style="padding-top:3px;">-1.45 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;"><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,24)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;SUNPHARMA</td></tr><tr><td>398.05</td></tr><tr><td style="padding-top:3px;">-1.69 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,25)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TATASTEEL</td></tr><tr><td>415.35</td></tr><tr><td style="padding-top:3px;">-6.39 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,26)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TCS</td></tr><tr><td>2116.30</td></tr><tr><td style="padding-top:3px;">-1.86 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,27)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TECHM</td></tr><tr><td>820.15</td></tr><tr><td style="padding-top:3px;">-1.13 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,28)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;TITAN</td></tr><tr><td>1279.80</td></tr><tr><td style="padding-top:3px;">-3.24 %</td></tr></tbody></table></td><td class="svboxred" style="width:75px;text-transform: capitalize;" onmouseover="innerdiv1(event,this,29)"><table cellpadding="0" cellspacing="0" border="0" style="text-align:center;width:100%"><tbody><tr><td>&nbsp;ULTRACEMCO</td></tr><tr><td>4397.20</td></tr><tr><td style="padding-top:3px;">-0.77 %</td></tr></tbody></table></td></tr><tr style="font-size:11px;cursor:pointer;text-align:center;color:blue"><td colspan="6" align="left" height="20px" valign="middle"><table width="100%"><tbody><tr><td align="left" valign="middle"></td><td style="font-size:13px; font-weight:normal; color:white;" align="right"><div class="text-left"><input type="button" value="Default View" class="btn btn-default" onclick="javascript:DivSwitch(0);"></div></td></tr></tbody></table></td></tr></tbody></table></div>
                    </div>
'''


table=soup.find_all('div',{'class':'heatamaparea largetable'})
print(table)

#for tr in soup.find_all('div',{'class':'heatamaparea largetable'}):
 #  tds = tr.find_all('td')
    
#print(tds)

#player_numbers = [ x.text for x in table.find_all('td')]


#print(player_numbers)
