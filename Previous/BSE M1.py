# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:21:53 2020

@author: india
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:19:24 2020

@author: india
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import time
from openpyxl import load_workbook
import re

counter=0
while True:
    data=['ASIAN PAINTS','AXIS BANK','BAJAJ AUTO','BAJAJ FINANCE','BHARTI AIRTEL','HCL TECHNOLOGIES','HDFC','HDFC BANK','HERO MOTOCORP','HUL','ICICI BANK','INDUSIND BANK','INFOSYS','ITC','KOTAK MAHINDRA BANK','LART','MAHM','MARUTI SUZUKI','NESTLE','NTPC','ONGC','POWER GRID','RELIANCE IND.','SBI','SUN PHARMA','TATA STEEL','TCS','TECH MAHINDRA','TITAN','ULTRATECH CEMENT']
    priceData=[]
    priceDataNew=[]
    foundStockName=[]
    datestime=[]
    
    
    
    for stockname in data:
        try:
            z = []
            URL="https://www.equitymaster.com/stockquotes/complist.asp?company="+str(stockname)
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            prices = soup.find('tr', attrs={'valign':'top'})
            datetime=soup.find('td', attrs={'class':'smallfont'}).text
            for a in prices.find('td', attrs={'class':'alignright'}):
                z=str(a)
                
                priceData.append(z.split("<")[0])
            foundStockName.append(stockname)
            datestime.append(datetime.strip()[:30])
        except:
            print("Data not found for stock " + str(stockname))
        
    for prise_data in priceData:
        if prise_data=="":
            pass
        else:
            priceDataNew.append(float(prise_data.replace(',','')))
        
    print(priceDataNew)
    
    dat1 = pd.DataFrame(foundStockName)
    dat1.columns = ['Stock Name']
    result1A = dat1
    
    dat2 = pd.DataFrame(result1A)
    dat3 = pd.DataFrame(priceDataNew)
    dat3.columns = ['Price(₨)']
    result2A = dat2.join(dat3)
    
    dat4 = pd.DataFrame(result2A)
    dat5=pd.DataFrame(datestime)
    dat5.columns=['Date and Time']
    result3A=dat4.join(dat5)
    
    
    
    try:
        writer.book=load_workbook('result.xlsx')
    except:
        df1.to_excel(writer,index=False,sheet_name='Sheet1',header=True)
        worksheet = writer.sheets['Sheet1']
        writer.save()
    else:
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader=pd.read_excel(r'result.xlsx')
        df1.to_excel(writer,index=False, sheet_name='Sheet1',header=False,startrow=len(reader)+1)
        worksheet = writer.sheets['Sheet1']
        writer.save()
    counter=counter+1
    
    time.sleep(1)
    if(counter==2):
        break