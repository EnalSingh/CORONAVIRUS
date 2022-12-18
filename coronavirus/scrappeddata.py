#from tkinter import *
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy
"""root = Tk()
root.title("Coronavirus Tracker")
root.geometry('1280x720+0+0')
root.iconbitmap('coronavirus.ico')"""

#importing URL
url="https://www.worldometers.info/coronavirus/#countries"

#requesting URL
web_data=requests.get(url).text


soup=BeautifulSoup(web_data,'lxml')



get_table=soup.find('table',id="main_table_countries_today")
get_table_data=get_table.tbody.find_all("tr")


di={}

for i in range(len(get_table_data)):
    try:
        key=get_table_data[i].find_all("a",href=True)[0].string
    except:
        key=get_table_data[i].find_all("td")[0].string

    values=[j.string for j in get_table_data[i].find_all("td")]   
    di[key]=values 

u=pd.DataFrame(di).loc[1:,:]
print(u)
    

    


#root.mainloop()
