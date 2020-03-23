
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
from openpyxl import load_workbook
import re
import time

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
    
    time.sleep(1)
    if(counter==1):
        break    
    
df2=pd.read_excel('result.xlsx', sheet_name='Sheet1')
df2=df2.sort_values(by='Stock Name')
print(df2)
writer1 = pd.ExcelWriter('Final.xlsx', engine='openpyxl')
df2.to_excel(writer1, sheet_name='Sheet1')
worksheet = writer1.sheets['Sheet1']
writer1.save()

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
df3=df3.join(data7)
df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')
df3['Date'] = df3['Date'].dt.date
#df3['Time']= pd.to_datetime(data['Time'])

df3.drop(['Date and Time'], axis = 1, inplace = True)

date_list = df3['Date'].values.tolist()
time_list = df3['Time'].values.tolist()
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
df3=df3.join(data8)
df3['Date and Time'] = pd.to_datetime(df3['Date and Time'], format='%Y-%m-%d')
df3.drop(['Date','Time'], axis = 1, inplace = True)
df3=df3.sort_values(by=['Stock Name', 'Date and Time'])

writer2 = pd.ExcelWriter('Final1.xlsx', engine='openpyxl')
df3.to_excel(writer2, sheet_name='Sheet1')
worksheet = writer2.sheets['Sheet1']
writer2.save()

