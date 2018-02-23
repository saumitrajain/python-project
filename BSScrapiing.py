# -*- coding: utf-8 -*-
"""
Spyder Editor

A cragislist crawler
"""

import urllib2
from bs4 import BeautifulSoup

city = "dallas"
obj = "piano"
min_price = 100
max_price = 1000
min_bedroom  =1
max_bedroom  =3
min_bath = 1
max_bath=3
#rent_page = "https://" + city + ".craigslist.org/search/apa?search_distance=0&min_price=" +str(min_price) +"max_price="+max_price +"&min_bedrooms="+min_bedroom+ "&max_bedrooms="+str(max_bedroom) +"&min_bathrooms="+str(min_bath) +"&max_bathrooms="+str(max_bath)+"&availabilityMode=0&sale_date=all+dates"
sale_page = "https://" + city + ".craigslist.org/search/sss?query=" + obj 


#rpage = urllib2.urlopen(rent_page)
spage = urllib2.urlopen(sale_page)


#soup = BeautifulSoup(rpage, "html.parser")
soup = BeautifulSoup(spage, "html.parser")

name_box = soup.find_all('p', attrs={'class': 'result-info'})
#price_box = soup.find_all('span', attrs={'class': 'result-price'})

i=0
f=open("craigs.txt","w+")
for name in name_box:   
    name_itr = "'"+str(name)+"'"    
    soup_item = BeautifulSoup(name_itr, "html.parser")    
    name_item = soup_item.find('a', attrs={'class': 'result-title hdrlnk'})    
    name_price =soup_item.find('span', attrs={'class': 'result-price'}) 
    f.write("****************************\n")
    f.write("Listing " + str(i) + " \n")
    itemname=name_item.text
    f.write(itemname.encode('utf-8')+"\n")
    if(name_price is None):
        f.write("Price not available\n")
    else:        
        price = name_price.text
        f.write(price.encode('utf-8')+"\n")
    f.write(name_item.get('href') + "\n")
    i=i+1
        
  
   