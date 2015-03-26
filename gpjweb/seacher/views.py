# -*- coding: utf-8 -*-
import time
import urllib2
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from seacher.models import Car
types=['不限','微型车','小型车','紧凑车型','中型车','大型车','豪华型车','跑车','MPV','SUV','商用车']
mileages = [0,1,3,6,65535]
mileagetext = ['不限','1万公里以内','1-3万公里','3-6万公里','6万公里以上']
prices = [0,3,5,8,10,15,20,30,50,65535]
pricetext = ['不限', '3万元以内', '3-5万元', '5-8万元', '8-10万元', '10-15万元', '15-20万元', '20-30万元', '30-50万元', '50万元以上']
carages = [0,1,3,5,8,50]
caragetext = ['不限', '1年以内', '1-3年', '3-5年', '5-8年', '8年以上']
def testweb(request):
    type = 0
    mileage = 0
    price = 0
    carage = 0
    if 'type' in request.GET:
        type = int(float(request.GET['type']))
    if 'mileage' in request.GET:
        mileage = int(float(request.GET['mileage']))
    if 'price' in request.GET:
        price = int(float(request.GET['price']))
    if 'carage' in request.GET:
        carage = int(float(request.GET['carage']))
    cars = Car.objects.all()
    if type!=0 :
        cars = cars.filter(type=types[type])
    if mileage != 0:
        cars = cars.filter(mileage__range=[mileages[mileage - 1],mileages[mileage]])
    if price != 0:
        cars = cars.filter(price__range=[prices[price - 1],prices[price]])
    if carage != 0:
        day = time.strftime("%d")
        month = time.strftime("%m")
        year = int(time.strftime("%Y"))
        now = [str(year -carages[carage - 1]), month, day]
        now = '-'.join(now)
        past = [str(year - carages[carage]), month, day]
        past = '-'.join(past)
        cars = cars.filter(licenseTime__range=[past, now])
    setting = {'type': type, 'mileage': mileage, 'price': price, 'carage': carage}
    settext = {'type': types[type], 'mileage': mileagetext[mileage], 'price': pricetext[price], 'carage': caragetext[carage]}
    params = {'cars': list(cars), 'setting': setting, 'settext': settext}
    return render_to_response('test.html', params)


def image(request):
    opener=urllib2.build_opener()
    url = request.GET['ref']
    headers=(("Referer", url),)
    opener.addheaders = headers
    img = opener.open(url)
    return HttpResponse(img, mimetype="image/jpeg")
