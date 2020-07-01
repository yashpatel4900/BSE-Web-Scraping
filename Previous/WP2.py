import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

ans="y"
data=['ASIAN PAINTS','AXIS BANK','BAJAJ AUTO','BAJAJ FINANCE','BHARTI AIRTEL','HCL TECHNOLOGIES','HDFC','HDFC BANK','HERO MOTOCORP','HUL','ICICI BANK','INDUSIND BANK','INFOSYS','ITC','KOTAK MAHINDRA BANK','LART','MAHM','MARUTI SUZUKI','NESTLE','NTPC','ONGC','POWER GRID','RELIANCE IND.','SBI','SUN PHARMA','TATA STEEL','TCS','TECH MAHINDRA','TITAN','ULTRATECH CEMENT']
priceData=[]
priceDataNew=[]
foundStockName=[]
datestime=[]

#while ans=="y":
 #   dataraw= str(input("Enter the name os stock: "))
  #  data.append(dataraw)
   # ans=str(input("Do you want to continue(y/n): "))

# for stockname in data:
#     z = []
#     URL="https://www.equitymaster.com/stockquotes/complist.asp?company="+str(stockname)
#     r = requests.get(URL)
#     soup = BeautifulSoup(r.content, 'html5lib')
#     prices = soup.find('tr', attrs={'valign':'top'})
#     for a in prices.find('td', attrs={'class':'alignright'}):
#         print(a)
#         for ff in a:
#             z.append(ff)
#         # z=str(a)
#     # print(z[0:4])
#     data2=""
#     for dat in z[0:4]:
#         data2+=dat
#     print(data2)
        # z= str(a)
	    # print(a[0:3])
    # prices2 = prices.findAll('span', attrs={'class':'IsqQVc NprOob i7KA_jMqO1Q8-zJFzKq8ukm8'})
    # priceData.append(prices2.text)


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
            # print(z.split("<")[0])
            priceData.append(z.split("<")[0])
        foundStockName.append(stockname)
        datestime.append(datetime)
    except:
        print("Data not found for stock " + str(stockname))

for prise_data in priceData:
    if prise_data=="":
        pass
    else:
        priceDataNew.append(prise_data)

print(priceDataNew)


dat1 = pd.DataFrame(foundStockName)
dat1.columns = ['Stock Name']
result1A = dat1

dat2 = pd.DataFrame(result1A)
dat3 = pd.DataFrame(priceDataNew)
dat3.columns = ['Price']
result2A = dat2.join(dat3)

dat4 = pd.DataFrame(result2A)
dat5=pd.DataFrame(datestime)
dat5.columns=['Date and Time']
result3A=dat4.join(dat5)



df1 = pd.DataFrame(result3A)
writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
writer.save()

'''
dat1 = pd.DataFrame(foundStockName)
dat1.columns = ['Stock Name']
result1A = dat1

dat2 = pd.DataFrame(result1A)
dat3 = pd.DataFrame(priceDataNew)
dat3.columns = ['Price']
result2A = dat2.join(dat3)

df1 = pd.DataFrame(result2A)
writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
writer.save()

'''