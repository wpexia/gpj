# Create your views here.
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from seacher.models import Car

def testweb(request):
    return render_to_response('test.html')


def make_model(request):
    f = open(r'C:/work/work/gpj/gpj/gpj_spider/data.json')
    st = f.readline()
    js = json.loads(st)
    car = Car()
    car.licenseTime = js['licenseTime'][0].encode("utf-8") + "-01"
    car.mileage = js['mileage'][0][0:-3].encode("utf-8")
    car.price = js['price'][0][1:-1].encode("utf-8")
    car.title = js['title'][0].encode("utf-8")
    car.img = js['img'][0].encode("utf-8")
    car.tags = json.dumps(js['tags'], ensure_ascii=False).encode("utf-8")
    car.url = js['url'].encode("utf-8")
    car.type = js['type'][0].encode("utf-8")
    car.transmission = js['transmission'][0].encode("utf-8")
    car.no = js['url'].split("/")[-1].split(".")[0].encode("utf-8")
    car.save()
    return HttpResponse()
