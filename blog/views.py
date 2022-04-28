from django.http import HttpResponse
from django.shortcuts import render

def posts_list(request):
    return HttpResponse('<h1>hello</h1>')
