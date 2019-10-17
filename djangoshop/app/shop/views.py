from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import search

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
def result(request,searchtext):
	return HttpResponse("You searched for %s" % searchtext)	

