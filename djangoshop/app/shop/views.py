from django.http import HttpResponse
from .models import search

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
def result(request,searchtext):
	response = "You searched for %s"
	return HttpResponse(response % searchtext)	
