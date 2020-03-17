from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")

def official_translation(request):
    # return HttpResponse("official translation!")
    return render(request, 'articles/article.html')




# Create your views here.
