from django.shortcuts import render

def home(request):
    return render(request ,'homepage.html')


def shop(request):
    return render(request , 'shopmain.html')

def news(request):
    return render(request , 'news.html')