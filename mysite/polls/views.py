from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.template.context_processors import request

def index(request):
    return HttpResponse("Hello!! This is my first django page")

def send_ls(request):
    output = subprocess.check_output("ls")
    print(output)
    return HttpResponse(output)
    

# Create your views here.
