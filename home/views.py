from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about_us(request):
    return render(request, 'info/about_us.html')


def faq(request):
    return render(request, 'info/faq.html')
