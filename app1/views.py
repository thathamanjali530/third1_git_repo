from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def smile(request):
    return HttpResponse('<h1><marquee>smile is very good medician in health</h1></marquee>')
def bangalore(request):
    return HttpResponse('bangalore is a very big city')