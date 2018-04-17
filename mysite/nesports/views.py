from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.core.signals import request_finished
from collections import OrderedDict
from django.http import Http404
from .models import Emp, Nfl, NflData, MlbData
import csv
import html


# Create your views here.
def home(request):
    return Http404("This is not a valid URL")

def images(request):
    return render(request, 'nesports/index.html')

def patriots(request):

    nfl = NflData.objects.filter(year='2017').extra(select={'val': 'passyards'}).order_by('val').reverse()[:30].values('team', 'player','touchdowns')

    return render(request, 'nesports/patriots.html', {'nfl': nfl, 'year': '2017', 'play': 'touchdowns', 'gran': 'player'})

def analyze(request):
    y = request.POST['year']
    play = request.POST['play']
    gran = request.POST['type']
    print("------------\nyear from the form = {}\n------------------\n".format(y))
    # nfl = NflData.objects.raw('Select * FROM nesports_nfldata')
    nfl = NflData.objects.filter(year=y).order_by(play).reverse()[:30].values('team', 'player', play)
    return render(request, 'nesports/patriots.html', {'nfl': nfl, 'year': y, 'play': play, 'gran': gran})

def analyzem(request):
    y = request.POST['year']
    play = request.POST['play']
    gran = request.POST['type']
    print("------------\nyear from the form = {}\n------------------\n".format(y))
    # nfl = NflData.objects.raw('Select * FROM nesports_nfldata')
    mlb = MlbData.objects.filter(year=y).order_by(play).reverse()[:30].values('team', 'player', play)
    return render(request, 'nesports/redsox.html', {'mlb': mlb, 'year': y, 'play': play, 'gran': gran})

def celtics(request):
    employees = Emp.objects.all()
    context = {
        'employees': employees
        }
    return render(request, 'nesports/celtics.html', context)

def redsox(request):
    mlb = MlbData.objects.filter(year='2017').extra(select={'val': 'homeruns'}).order_by('val').reverse()[:20].values('team', 'player', 'homeruns')
    return render(request, 'nesports/redsox.html', {'mlb': mlb, 'year': '2017', 'play': 'homeruns', 'gran': 'player'})

def random(request, num):
    employees = Emp.objects.count()
    if int(num) > employees:
        raise Http404("There are only {} objects in Employee you passed {}".format(employees, num))
    return HttpResponse('<h2>I am :'+ num + '</h2>')

def sqltabs(request):
    html = ''
    employees = Emp.objects.all()
    for employee in employees:
        url = '/index/'+str(employee.id)+'/'
        html += '<a href="'+ url + '">' + employee.name + '</a><br>'
    return HttpResponse(html)


def bruins(request):
    return render(request, 'nesports/bruins.html')
