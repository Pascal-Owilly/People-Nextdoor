from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'neighbourhood/index.html')


def profile(request):
    return render(request, 'neighbourhood/profile.html')