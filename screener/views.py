
from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def screener(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())


def ticket(request):
  template = loader.get_template('ticket.html')
  return HttpResponse(template.render())
