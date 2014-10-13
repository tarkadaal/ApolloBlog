from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, world, is it me you\'re looking for?')