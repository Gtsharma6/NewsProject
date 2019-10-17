from django.shortcuts import render
from django.http import HttpResponse
from news1.models import AddUser
from django.views import View
from news1 import api
import json
import requests
import smtplib

def index(request):
    return render(request,"layout.html")

def Signup(request):
    return render(request,"Signup.html")

def Login(request):
    return render(request,"Login.html")

def Contact(request):
    return render(request,'Contact.html')

def Signup_t(request):
    if (request.POST):
        signup_data = request.POST.dict()

        #if signup_data["Password"] == signup_data["Cpassword"]:
           # del signup_data["Cpassword"]
        del signup_data["csrfmiddlewaretoken"]
        try:
            AddUser.objects.get(Email= signup_data["Email"])
        except AddUser.DoesNotExist as e:
                    
                    new_user = AddUser.objects.create(**signup_data)
                    new_user.save()
                    #email
                    x = smtplib.SMTP_SSL('smtp.googlemail.com',465)
                    x.login("robot11@gmail.com","robot@4567")
                    message = "thanks for subscribing"
                    x.sendmail("robot11@gmail.com", signup_data["Email"],message)
                    x.quit()

                    error = "Thanks for subscribing TOPNEWS"
                    return render(request,"Login.html",{"title": "TOPNEWS","error":error })
        else:
            error = "User already exists"
            return render(request,"Signup.html",{"error":error})
        #else:
            #error ="Password doesn't match"
           # return render(request,"Login.html",{"error":error})
   #else:
        #error = "Post method didnt get try again"
        #return render(request,"Login.html",{"errror":error})     

def newsh(request):
    data1 = api.xyz
    print(data1)
    d = []
    for i in data1:
        newspaper1 ={
            "author": i[0],
            "title": i[1],
            "description": i[2],
            "url": i[3],
            "content": i[4],
        }
        d.append(newspaper1)
    return render(request,"layout.html",{"data":d})    


def weather(request):
    url = ('http://openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
    response = requests.get(url).json()
    content1 = json.dumps(response,indent=4)
    content = json.loads(content1)
    print(content)

    weather_data={
        "weather_sta" :content["weather"][0]["description"],
        "weather_temp":content["main"]["humidity"],
        "weather_ttemp":content["main"]["temp_max"],
        "weather_t2temp":content["main"]["temp_min"],
    }
    return render(request,"weather.html",{"x":weather_data})
        

        
