from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.


def HelloWorld(request):
    ctx = {
        "msg":"Hello World!"
    }
    return HttpResponse(json.dumps(ctx))