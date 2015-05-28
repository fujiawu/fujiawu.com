from django.shortcuts import *

def home(request):
          return render(request, 'home.html')

def experience(request):
          return render(request, 'experience.html')

def research(request):
          return render(request, 'research.html')

def publication(request):
          return render(request, 'publication.html')

def others(request):
          return render(request, 'others.html')
