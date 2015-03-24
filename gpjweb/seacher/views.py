# Create your views here.
from django.shortcuts import render_to_response

def testweb(request):
    return render_to_response('test.html')