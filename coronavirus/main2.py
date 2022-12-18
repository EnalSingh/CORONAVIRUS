
import webbrowser
import covid                              
import tkinter as tk
import matplotlib.pyplot as plt            
import pandas as pd
from tkinter import *


#gui for main window

root = Tk()
root.title("Coronavirus info system")
root.geometry('1920x1080+0+0')
root.configure(bg='darkorange')
root.iconbitmap('coronavirus.ico')

randomframe=Frame(root,borderwidth=6,bg="darkorange",relief=GROOVE)
randomframe.pack(side=TOP,fill="x")

#Label For main window

Introlabel = Label(randomframe,text='Coronavirus Info System',
font=('Times', 40, 'italic bold '),bg="darkorange")
Introlabel.config(anchor=CENTER)
Introlabel.pack(fill=BOTH)

label2 = Label(randomframe, text='An Initiative By City International School',
font=('Arial', 15),
bg='darkorange')
label2.config(anchor=CENTER)
label2.pack(pady=5)
label2.pack()


def tracker():
    
    def show_data():
        
        data = covid.Covid()
        country_name = e1.get()
        status = data.get_status_by_country_name(country_name)
        Active = status['active']
        e2.insert(0,Active)
        Death = status['deaths']
        e3.insert(0, Death)
        Confirm = status['confirmed']
        e4.insert(0, Confirm)
        Recover = status['recovered']
        e5.insert(0, Recover)
        print(status)
        
        # intialise data of lists.
        data = {'id': status['id'],
            'Country': status['country'],
            'Confirmed': status['confirmed'],
            'Active': status['active'],
            'Deaths': status['deaths'],
            'Recovered': status['recovered'],
            'Latitude': status['latitude'],
            'Longitude': status['longitude'],
            'Last_Updated': status['last_update']
            }
        
        # Create DataFrame
        df = pd.DataFrame(data, index=[0])
        # Print the output.
        print(df)
        
        cadr = {

        key:status[key]
        for key in status.keys() & {"confirmed","active","deaths","recovered"}
        }
        n = list(cadr.keys())
        v = list(cadr.values())
        plt.title("Country")
        plt.bar(range(len(cadr)),v,tick_label=n,label=('active'))
        plt.xlabel('x-labels')
        plt.ylabel('Data')

        plt.plot(range(len(cadr)))


        plt.show()
    
    master = tk.Tk()
    master.title('Covid-19 country status ')
    master.configure(bg='darkorange')
    tk.Label(master,text="COVID-19 COUNTRY STATUS" ,padx=50,bg='darkorange').grid(row=0)
    tk.Label(master, text="Enter your Country name : -",bg='darkorange').grid(row=2)
    e1 = tk.Entry(master)
    e1.grid(row=2, column=3)
    tk.Button(master,text='Show', command=show_data).grid(row=5,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)


    tk.Label(master, text="Active Cases : -",bg='darkorange').grid(row=8)

    e2 = tk.Entry(master)
    e2.grid(row=8, column=3)

    tk.Label(master, text="Death Cases : -",bg='darkorange').grid(row=9)
    e3 = tk.Entry(master)
    e3.grid(row=9, column=3)

    tk.Label(master, text="Confirmed Cases : -",bg='darkorange').grid(row=10)
    e4 = tk.Entry(master)
    e4.grid(row=10, column=3)

    tk.Label(master, text="Recovered Cases : -",bg='darkorange').grid(row=11)
    e5 = tk.Entry(master)
    e5.grid(row=11, column=3)
    master.mainloop()
    
#function for dasboard gui   
def dash():
    def dashbar():
        webbrowser.open("https://covid19.who.int/")
    who = Tk()
    who.title("Coronavirus info system")
    who.geometry('1400x720')
    who.configure(bg='darkorange')
    who.iconbitmap('coronavirus.ico')
    
    frame1=Frame(who,borderwidth=8,bg="darkorange",relief=SUNKEN)
    frame1.pack(side=TOP,fill="x")
    
    label5=Label(frame1,text="Covid-19 Dashboard",font=("Times", 40,"bold italic underline"),bg="darkorange")
    label5.pack(pady=10)
    
    frame2=Frame(who,borderwidth=5,relief=GROOVE,bg="lightcoral")
    frame2.pack(side=LEFT,fill="y",pady=50)
    
    label8=Label(frame2,text="The World Health Organization (WHO) on March 11 declared COVID-19 a pandemic, pointing\n to the over 118,000 cases of the coronavirus illness in over 110 countries and\nterritories around the world and the sustained risk of further global spread.\n“This is not just a public health crisis, it is a crisis that will touch every sector,”\nsaid Dr. Tedros Adhanom Ghebreyesus, WHO director-general, at a media\nbriefing. “So every sector and every individual must be involved in the fights.”\nAn epidemic refers to an uptick in the spread of a disease within a specific\ncommunity. By contrast, the WHO defines a pandemic as global spread of a new \ndisease, though the specific threshold for meeting that criteria is fuzzy.\nThe term is most often applied to new influenza strains, and the CDC says\nit’s used when viruses “are able to infect people easily and spread from person to\nperson in an efficient and sustained way” in multiple regions. The declaration\nrefers to the spread of a disease, rather than the severity of the illness it causes  ",
                 font=('Times', 15 ,'italic bold'),
                 bg='lightcoral',justify=LEFT)
    
    label8.pack(pady=10)
    
    dashbutton=Button(frame2,fg="black",relief=RIDGE,text="COVID19 DASHBAR",font=('Times',20,'bold underline italic'),bg="olive",width=20,height=2,command=dashbar)
    dashbutton.pack(pady=20)
    
    pframe=Frame(who,borderwidth=5,relief=SUNKEN,bg='olive')
    pframe.pack(side=TOP,fill="x",padx=10,pady=50)
    
    dashlab=Label(pframe,text="To prevent infection and to slow transmission of COVID-19,\ndo the following:",
                  font=('Helvetica',15,'bold italic underline'),bg="olive",justify=LEFT)
    dashlab.pack()
    
    
    ppframe=Frame(who,bg='darkorange',borderwidth=4)
    ppframe.pack(side=TOP,fill="both",padx=10)
    dashlab2=Label(ppframe,text="●Wash your hands regularly with soap and water, or clean\nthem with alcohol-based hand rub.\n\n●Maintain at least 1 metre distance between you and people \ncoughing or sneezing.\n\n●Avoid touching your face.\n\n●over your mouth and nose when coughing or sneezing.\n\n●Stay home if you feel unwell.\n\n●Refrain from smoking and other activities that weaken the lungs.\n\n●Practice physical distancing by avoiding unnecessary\ntravel and staying away from large groups of people.",
                   font=('Times',15,'italic'),bg="darkorange",justify=LEFT)
    dashlab2.pack()
    
    
    who.mainloop()
        
def ayurved():
    def guideline():
        webbrowser.open("https://www.ayurvedacollege.com/blog/corona-virus-precautions-and-guidelines/")
    ayur = Tk()
    ayur.title("Coronavirus info system")
    ayur.geometry('1400x720')
    ayur.configure(bg='olive')
    ayur.iconbitmap('coronavirus.ico')
    
    ayurframe=Frame(ayur,borderwidth=5,bg="darkorange",relief=GROOVE)
    ayurframe.pack(side=TOP,fill="x")
    
    ayurlabel=Label(ayurframe,text="Ayurveda Guidelines",font=('Times',40,'bold italic'),bg='darkorange')
    ayurlabel.pack()
    
    ayurframe2=Frame(ayur,borderwidth=4,bg="darkorange",relief=SUNKEN)
    ayurframe2.pack(side=TOP,pady=20)
    
    ayurlabel2=Label(ayurframe2,text="Ayurveda, being the science of life, propagates the gifts of nature in maintaining\nhealthy and happy living. Ayurveda’s extensive knowledge base on preventive \ncare, derives from the concepts of “Dinacharya” - daily regimes and “Ritucharya”\n- seasonal regimes to maintain healthy life. It is a plant-based science. The \nsimplicity of awareness about oneself and the harmony each individual can achieve \nby uplifting and maintaining his or her immunity is emphasized across Ayurveda’s \nclassical scriptures.\n\nMinister of State (MoS) for AYUSH, Shripad Y Naik  said that Prime Minister\nNarendra Modi has established a task force for scientific validation of Ayurveda\nand traditional medicine formulas through research institutions like ICMR, to\nbe used in the treatment of COVID-19.",
                     font=('Times', 15 ,'italic bold'),
                 bg='darkorange',justify=LEFT)
    
    ayurlabel2.pack(pady=10)
    
    ayurframe3=Frame(ayur,borderwidth=4,bg='darkorange',relief=SUNKEN)
    ayurframe3.pack(side=TOP)
    
    ayurlabel3=Label(ayurframe3,text="California College",font=('Helvetica',20,'bold underline italic')
                     ,bg='darkorange')
    ayurlabel3.pack()
    
    ayurframe4=Frame(ayur,borderwidth=3,relief=SUNKEN,bg='darkorange')
    ayurframe4.pack()
    
    ayurlabel4=Label(ayurframe4,text="Among the countries with the highest death toll are some of the most populour countries in \nthe world such as the US, Brazil, and Mexico.You can see\nthe ayurveda guidlines by california college for coronavirus by clicking the button below:"
                     ,font=('Times',17,'italic'),bg='darkorange',justify=CENTER)
    ayurlabel4.pack()
    
    ayurbutton=Button(ayurframe4,borderwidth=3,fg="black",relief=GROOVE,text="Ayurveda Guidelines",font=('Times',15,'bold underline italic'),bg="olive",width=20,height=2,command=guideline)
    ayurbutton.pack(pady=10)
    
    ayur.mainloop()
        
    
def credit(): 
    cred = Tk()
    cred.title("Coronavirus info system")
    cred.configure(bg='darkblue')
    cred.iconbitmap('coronavirus.ico')
    cred.geometry("900x400")
    
    credframe=Frame(cred,borderwidth=3,relief=GROOVE,bg='yellow')
    credframe.pack(side=TOP,fill="x",padx=10)
    
    credlabel=Label(credframe,text='Coronavirus info system',font=('Helvetica',20,'bold'),
                    bg='yellow',fg='purple')
    credlabel.pack()
    
    credframe2=Frame(cred,borderwidth=2,relief=SUNKEN,bg='yellow')
    credframe2.pack(side=TOP,pady=20,padx=10)
    
    credlabel2=Label(credframe2,text="Designed By:-",font=('Times',20,'underline'),bg='yellow',fg='purple')
    credlabel2.pack()
    
    credframe3=Frame(cred,borderwidth=5,relief=SUNKEN,bg='darkblue')
    credframe3.pack(side=TOP,fill="y",pady=10,padx=10)
    
    credlabel3=Label(credframe3,text="● Enal Singh (12-Science)\n\n ● Danish Khan (12-Science)",font=('Times',17),bg='darkblue',fg='yellow')
    credlabel3.pack()
    
    credframe4=Frame(cred,borderwidth=5,relief=SUNKEN,bg='yellow')
    credframe4.pack(side=TOP,fill="y",pady=9,padx=10)
    
    credlabel4=Label(credframe4,text="CITY INTERNATIONAL SCHOOL\nLUCKNOW 226016",font=('Times',17),bg='yellow',fg='purple',justify=CENTER)
    credlabel4.pack()
    
    credframe5=Frame(cred,borderwidth=5,relief=SUNKEN,bg='darkblue')
    credframe5.pack(side=TOP,fill="y",pady=9,padx=10)
    
    credlabel5=Label(credframe5,text="SUBIMTTED TO:-Rachna Ma'am",font=('Times',17),bg='darkblue',fg='yellow',justify=CENTER)
    credlabel5.pack()
    
    
    cred.mainloop()
    
    
    
f1=Frame(root,borderwidth=6,bg="darkorange")
f1.pack(side=TOP,fill="y",pady=10) 
    
    
button=Button(f1,fg="red",relief=SOLID,text="Tracker",font=('Times',15,'bold underline italic'),bg="green",width=20,height=2,activebackground="lightcoral",activeforeground="red",command=tracker)
button.pack(side=LEFT,padx=35)

button2=Button(f1,fg="blue",relief=SOLID,text="Dashboard",font=('Times',15,'bold underline italic'),bg="green",width=20,height=2,activebackground="lightcoral",activeforeground="blue",command=dash)
button2.pack(side=LEFT,padx=35)

button3=Button(f1,fg="black",relief=SOLID,text="Ayush Ministry ",font=('Times',15,'bold underline italic'),bg="green",width=20,height=2,activebackground="lightcoral",activeforeground="green",command=ayurved)
button3.pack(side=LEFT,padx=35)

button4=Button(f1,fg="brown",relief=SOLID,text="Credits",font=('Times',15,'bold underline italic'),bg="green",width=20,height=2,activebackground="lightcoral",activeforeground="brown",command=credit)
button4.pack(side=LEFT,padx=35)

def report():
    webbrowser.open("https://labreports.upcovid19tracks.in/")

flabel=Frame(root,borderwidth=6,bg="orange",relief=SUNKEN)
flabel.pack(side=LEFT,fill="both",pady=0)

label3= Label(flabel,text='What Is Coronavirus ?',
font=('Helvetica',30,'bold'),
bg='orange')
label3.pack(pady=10)
label3.pack()

label4 = Label(flabel, text='Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.\nMost people infected with the COVID-19 virus will experience mild to moderate respiratory illness and\n recover without requiring special treatment.  Older people, and those with underlying medical problems\n like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to \ndevelop serious illness.The best way to prevent and slow down transmission is\n be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect\n yourself and others from infection by washing your hands or using an alcohol\n based rub frequently and not touching your face. The COVID-19 virus spreads primarily through droplets\n of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important\n that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).\nAt this time, there are no specific vaccines or treatments for COVID-19. However, \nthere are many ongoing clinical trials evaluating potential treatments. \nWHO will continue to provide updated information as soon as clinical findings become available.',
font=('Times', 15 ,'italic bold'),
bg='orange',justify=CENTER)

label4.pack(pady=10)
label4.pack()

label6=Label(flabel,text="!!COVID-19 Vaccine !!",font=('Helvetica',20,'bold underline'),bg="orange")
label6.pack(pady=10)

label7=Label(flabel,text="There are currently more than 100 COVID-19 vaccine candidates under development,with a number of these in the human\ntrial phase. WHO is working in collaboration with scientists, business, and global health organizations through the ACT\nAccelator speed up the pandemic response. When a safe and effective vaccine is found, COVAX (led by WHO, GAVI and  CEPI)\nwill facilitate the equitable access and distribution of these vaccines to protect people in all countries. \nPeople most at risk will be prioritized.",
             font=('Times', 15 ,'italic bold'),
bg='orange',justify=CENTER)
label7.pack(pady=20)

reportbutton=Button(flabel,borderwidth=3,relief=RIDGE,text="Check Your COVID Report",font=('Times',15,'bold underline italic'),bg="orange",fg="red",width=30,height=2,command=report)
reportbutton.pack(pady=10)


photoframe=Frame(root,borderwidth=5,relief=SUNKEN)
photoframe.pack(side=BOTTOM,fill="y",padx=5)

photo=PhotoImage(file="warriors.png")
photolabel=Label(photoframe,image=photo)
photolabel.pack()


photoframe2=Frame(root,borderwidth=5,relief=SUNKEN)
photoframe2.pack(side=RIGHT,fill="y",padx=5,pady=3)

photo2=PhotoImage(file="distancing.png")
photolabel2=Label(photoframe2,image=photo2)
photolabel2.pack()


root.mainloop()
