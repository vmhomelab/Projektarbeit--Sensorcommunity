"""sensorino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

def getTempForAYear(request):
    cursor = connection.cursor()
    dates = []
    temperature = []
    humidity = []
    try:
       with cursor.execute('SELECT ROUND(AVG(temperature),2) AS avg_temperatur,ROUND(AVG(humidity),2) AS avg_luft, CAST(timestamp AS DATE) AS Datum FROM dbo.sensor_dht GROUP BY CAST(timestamp AS DATE) ORDER BY CAST(timestamp AS DATE);'):
        row = cursor.fetchone()
        while row:
            dates.append(row[2])
            humidity.append(row[1])
            temperature.append(row[0])
            row = cursor.fetchone()
    finally:
        cursor.close()
    return JsonResponse({'dates' : dates, 'temperature' : temperature, 'humidity' : humidity},safe=False)

def getTemperatur(request) :
    print(request.GET.get('month'),request.GET.get('year'))
    cursor = connection.cursor()
    dates = []
    temperature = []
    try:
        sql = 'SELECT ROUND(AVG(temperature),2) AS avg_temperatur, CAST(timestamp AS DATE) AS Datum FROM dbo.sensor_dht WHERE MONTH(timestamp) = '+request.GET.get('month')+' AND YEAR(timestamp) = '+request.GET.get('year')+' GROUP BY CAST(timestamp AS DATE) ORDER BY CAST(timestamp AS DATE);'
        with cursor.execute(sql):
            row = cursor.fetchone()
            while row:
                dates.append(row[1])
                temperature.append(row[0])
                row = cursor.fetchone()
    finally:
        cursor.close()
    return JsonResponse({'dates' : dates, 'temperature' : temperature},safe=False)

def getLuftfeuchtigkeit(request) :
    print(request.GET.get('month'),request.GET.get('year'))
    cursor = connection.cursor()
    dates = []
    luftfeuchtigkeit = []
    try:
        sql = 'SELECT ROUND(AVG(humidity),2) AS avg_humidity, CAST(timestamp AS DATE) AS Datum FROM dbo.sensor_dht WHERE MONTH(timestamp) = '+request.GET.get('month')+' AND YEAR(timestamp) = '+request.GET.get('year')+' GROUP BY CAST(timestamp AS DATE) ORDER BY CAST(timestamp AS DATE);'
        with cursor.execute(sql):
            row = cursor.fetchone()
            while row:
                dates.append(row[1])
                luftfeuchtigkeit.append(row[0])
                row = cursor.fetchone()
    finally:
        cursor.close()
    return JsonResponse({'dates' : dates, 'luftfeuchtigkeit' : luftfeuchtigkeit},safe=False)

def index(request):
    return render(request,'index.html')

def temperatur(request):
    return render(request, 'temperatur.html')

def luftfeuchtigkeit(request):
    return render(request, 'luftfeuchtigkeit.html')

urlpatterns = [
    path('api/tempyear',getTempForAYear),
    path('api/temperatur',getTemperatur),
    path('api/luftfeuchtigkeit',getLuftfeuchtigkeit),
    path('temperatur', temperatur),
    path('luftfeuchtigkeit', luftfeuchtigkeit),
    path('',index),
]
