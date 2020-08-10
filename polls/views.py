from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.

def health(request):
    msg = "Hello world!, you are at health index of testing django application"

    return HttpResponse(json.dumps(msg, default=str, indent=4), content_type="application/json")