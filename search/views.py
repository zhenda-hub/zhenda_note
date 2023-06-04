from django.shortcuts import render, redirect

# Create your views here.


def get_search(request):
    return render(request, 'search.html')