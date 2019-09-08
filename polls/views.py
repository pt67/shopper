from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'templates/index.html')

def blog(request):
    return render(request, 'templates/blog.html')

def about(request):
    return render(request, 'templates/about.html')

def portfolio(request):
    return render(request, 'templates/portfolio.html')

def contact(request):
    return render(request, 'templates/contact.html')

def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def results(request, product_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % product_id)

def vote(request, product_id):
    return HttpResponse("You're voting on product %s." % product_id)
