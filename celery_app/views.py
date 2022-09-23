from turtle import delay
from django.shortcuts import render
from django.http import HttpResponse
from .helper import send_mail_without_celery
from .task import *
# Create your views here.


def index(request):
    kwargs = {}
    args = ['https://www.python.org/downloads/']
    scrape_data.apply_async(args=args, kwargs=kwargs)
    return HttpResponse('<h1> Data scraped </h1>')
