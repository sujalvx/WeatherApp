# Weather App By Sujal Verma
APIkey =''
# All imports.
from tkinter import *
from PIL import ImageTk,Image
from geopy.geocoders import Nominatim
from tkinter import messagebox
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz
import requests

# Tkinter Window
main = Tk()
main.geometry('900x500')
main['background'] = 'white'
main.resizable(False,False)
main.iconbitmap("C:/Wallpaper/VScode.ico")
main.title("Weather App")

# Inserting required images and labeling important texts. 
searchbar = ImageTk.PhotoImage(Image.open("C:/Wallpaper/googlesearch.jpg"))
search = Label(main,image=searchbar,bd=0)
search.place(x=300,y=220)

query = Entry(main,width=20,font=("Arial Black",10,'bold'),bg='#0b0a0a',foreground='White',bd=0,justify='center')
query.place(x=380,y=230)

magnisearch = ImageTk.PhotoImage(Image.open("C:/Wallpaper/googles.jpg"))

weatherimage = ImageTk.PhotoImage(Image.open("C:/Wallpaper/weather.jpg"))
weaimage = Label(main,image=weatherimage,bd=0)
weaimage.place(x=358,y=4)

windimage = ImageTk.PhotoImage(Image.open("C:/Wallpaper/wind.jpg"))
wind = Label(main,image=windimage,bd=0)
wind.place(x=60,y=360)
humidityimage = ImageTk.PhotoImage(Image.open("C:/Wallpaper/humidity.jpg"))
humidity = Label(main,image=humidityimage,bd=0)
humidity.place(x=260,y=340)
pressureimage = ImageTk.PhotoImage(Image.open("C:/Wallpaper/pressure.jpg"))
pressure = Label(main,image=pressureimage,bd=0)
pressure.place(x=460,y=300)

c = Label(main,font=('Arial Black',10,'bold'),bg='white')
c.place(x=545,y=160)
t = Label(main,font=('Arial Black',50,'bold'),bg='white',foreground='Red')
t.place(x=558,y=40)
w = Label(main,text='...',bd=0,font=('Arial Black',10,'bold'),bg='white')
w.place(x=80,y=440)
h = Label(main,text='...',bd=0,font=('Arial Black',10,'bold'),bg='white')
h.place(x=290,y=440)
p = Label(main,text='...',bd=0,font=('Arial Black',10,'bold'),bg='white')
p.place(x=490,y=440)
d = Label(main,text='...',bd=0,font=('Arial Black',10,'bold'),bg='white')
d.place(x=663,y=440)
boysphoto = ImageTk.PhotoImage(Image.open("C:/Wallpaper/boys.jpg"))
boys = Label(main,image=boysphoto,bd=0)
boys.place(x=620,y=330)

#Creating Method to build logic for our weather app
def weather():
    try :
        city = query.get()
        geolocater = Nominatim(user_agent="geoapiExercises")
        location = geolocater.geocode(city)
        clay = TimezoneFinder()
        result = clay.timezone_at(lng=location.longitude,lat=location.latitude)
        home = pytz.timezone(result)
        localtime = datetime.now(home)
        currenttime =localtime.strftime("%I:%M %p")
        clock.config(text=currenttime)
        # name.config(text=f'CURRENT WEATHER of')
        name2.config(text=city)

        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={APIKEY}"

        jsondata = requests.get(api).json()
        condition1 = jsondata['weather'][0]['description']
        temp1 = int(jsondata['main']['temp']-273.15)
        pressure1 = jsondata['main']['pressure']
        humidity1 = jsondata['main']['humidity']
        wind1 = jsondata['wind']['speed']

        t.config(text=(temp1,"°"))
        c.config(text=f'{condition1} | FEELS LIKE {temp1} °')
        w.config(text=f'{wind1} km/h')
        p.config(text=f'{pressure1} Pa')
        h.config(text=f'{humidity1} %' )
        d.config(text=condition1)

    except Exception as E:
        messagebox.showerror("Weather App","Invalid Entry")
    


search = Button(main,image=magnisearch,command=weather,bd=0)
search.place(x=640,y=229)

name2 = Label(main,font=("Algerian",26,'bold'),foreground='Black',bd=0,bg='white')
name2 .place(x=532,y=10)

#Clock to see time.
clock = Label(main,font=("Stencil",14),foreground='Black',bd=0,bg='white')
clock.place(x=552,y=130)

#Ending 
main.mainloop()

#Please create your own API key to use this application. Thank You
