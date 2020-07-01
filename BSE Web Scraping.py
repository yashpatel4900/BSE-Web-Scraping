# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:19:24 2020

@author: india
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
from openpyxl import load_workbook
import re
import time
import numpy as numpy
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
>>>>>>> 604ae63c0f1158be9344eefab2d198fffc42770f


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
            datestime.append(datetime.strip()[11:30])
        except:
            print("Data not found for stock " + str(stockname))
        
    for prise_data in priceData:
        if prise_data=="":
            pass
        else:
            priceDataNew.append(float(prise_data.replace(",","")))
        
    print(priceDataNew)
    
    dat1 = pd.DataFrame(foundStockName)
    dat1.columns = ['Stock Name']
    result1A = dat1
    
    dat2 = pd.DataFrame(result1A)
    dat3 = pd.DataFrame(priceDataNew)
    dat3.columns = ['BSE Price(₨)']
    result2A = dat2.join(dat3)
    
    dat4 = pd.DataFrame(result2A)
    dat5=pd.DataFrame(datestime)
    dat5.columns=['Date and Time']
    result3A=dat4.join(dat5)
    
    df1 = pd.DataFrame(result3A)
    
    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl')
    
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
    
    time.sleep(180)
    if(counter==20):
        break    
    
df2=pd.read_excel('result.xlsx', sheet_name='Sheet1')
<<<<<<< HEAD

from datetime import datetime, date
date_list = df2['Date and Time'].values.tolist()
date_listNew=[]
date_listNew1=[]
for a in date_list:
    date_listNew.append(a[0:6]+str(" 20"))
    
for a in date_listNew:
    date_object = datetime.strptime(a, '%b %d %y').date()
    date_listNew1.append(date_object)
    
time_list = df2['Date and Time'].values.tolist()
time_listNew=[]
time_listNew1=[]
for a in time_list:
    time_listNew.append(a[7:])
    
for a in time_listNew:
    time_object = datetime.strptime(a, '%I:%M:%S %p').time()
    time_listNew1.append(time_object)
    
data6=pd.DataFrame(date_listNew1)
data7=pd.DataFrame(time_listNew1)
data6.columns=['Date']
data7.columns=['Time']
df3=df2.join(data6)
df4=df3.join(data7)
df4['Date'] = pd.to_datetime(df4['Date'], format='%Y-%m-%d')
df4['Date'] = df4['Date'].dt.date
#df3['Time']= pd.to_datetime(data['Time'])

df4.drop(['Date and Time'], axis = 1, inplace = True)

date_list = df4['Date'].values.tolist()
time_list = df4['Time'].values.tolist()
timel=[]
for a in time_list:
    timel.append(str(a))
datel=[]
for a in date_list:
    datel.append(str(a))
dtl=[]
for (a,b) in zip(datel,timel):
    c=str(a)+" "+str(b)
    dtl.append(c)

data8=pd.DataFrame(dtl)
data8.columns=['Date and Time']
df5=df4.join(data8)
df5['Date and Time'] = pd.to_datetime(df5['Date and Time'], format='%Y-%m-%d')
df5.drop(['Date','Time'], axis = 1, inplace = True)
df6=df5.sort_values(by=['Stock Name', 'Date and Time'])

pre=0

def apply_color(val):
    global pre
    color=''
    if val<pre:
        if abs(val-pre)*100/val >10:
            color='black'
        else:    
            color='red'
    elif val>pre:
        if abs(val-pre)*100/val >10:
            color='black'
        else:    
            color='green'
    else:
        color='blue'
    
    pre=val
    return 'color: %s' %color
        
    

s=df6.style.applymap(apply_color, subset=['BSE Price(₨)'])

writer = pd.ExcelWriter('Final.xlsx', engine='openpyxl')
s.to_excel(writer, index=False,  sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
writer.save()

df6.reset_index(inplace = True)

for i in range(0,len(df6),len(df6)//30):
    x=list(df6['Date and Time'][i:i+len(df6)//30])
    y=list(df6['BSE Price(₨)'][i:i+len(df6)//30])
    fig=plt.figure()
    axes=fig.add_axes([.1,.1,1,1])
    axes.plot_date(x,y,'r-',marker='*',label=df6['Stock Name'][i])
    axes.set_title('Stock Prices')
    axes.set_xlabel('Timeline')
    axes.set_ylabel('Price')
    axes.legend()
    fig.savefig('%s.' %df6['Stock Name'][i],dpi=300,bbox_inches='tight')
=======
>>>>>>> 604ae63c0f1158be9344eefab2d198fffc42770f

from datetime import datetime, date
date_list = df2['Date and Time'].values.tolist()
date_listNew=[]
date_listNew1=[]
for a in date_list:
    date_listNew.append(a[0:6]+str(" 20"))
    
for a in date_listNew:
    date_object = datetime.strptime(a, '%b %d %y').date()
    date_listNew1.append(date_object)
    
time_list = df2['Date and Time'].values.tolist()
time_listNew=[]
time_listNew1=[]
for a in time_list:
    time_listNew.append(a[7:])
    
for a in time_listNew:
    time_object = datetime.strptime(a, '%I:%M:%S %p').time()
    time_listNew1.append(time_object)
    
data6=pd.DataFrame(date_listNew1)
data7=pd.DataFrame(time_listNew1)
data6.columns=['Date']
data7.columns=['Time']
df3=df2.join(data6)
df4=df3.join(data7)
df4['Date'] = pd.to_datetime(df4['Date'], format='%Y-%m-%d')
df4['Date'] = df4['Date'].dt.date
#df3['Time']= pd.to_datetime(data['Time'])

df4.drop(['Date and Time'], axis = 1, inplace = True)

date_list = df4['Date'].values.tolist()
time_list = df4['Time'].values.tolist()
timel=[]
for a in time_list:
    timel.append(str(a))
datel=[]
for a in date_list:
    datel.append(str(a))
dtl=[]
for (a,b) in zip(datel,timel):
    c=str(a)+" "+str(b)
    dtl.append(c)

data8=pd.DataFrame(dtl)
data8.columns=['Date and Time']
df5=df4.join(data8)
df5['Date and Time'] = pd.to_datetime(df5['Date and Time'], format='%Y-%m-%d')
df5.drop(['Date','Time'], axis = 1, inplace = True)
df6=df5.sort_values(by=['Stock Name', 'Date and Time'])

pre=0

def apply_color(val):
    global pre
    color=''
    if val<pre:
        if abs(val-pre)*100/val >10:
            color='black'
        else:    
            color='red'
    elif val>pre:
        if abs(val-pre)*100/val >10:
            color='black'
        else:    
            color='green'
    else:
        color='blue'
    
    pre=val
    return 'color: %s' %color
        
    

s=df6.style.applymap(apply_color, subset=['BSE Price(₨)'])

writer = pd.ExcelWriter('Final.xlsx', engine='openpyxl')
s.to_excel(writer, index=False,  sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
writer.save()
