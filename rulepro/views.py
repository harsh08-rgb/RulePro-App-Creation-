from django.shortcuts import render

# Home page view
def home(request):
    return render(request, "rulepro/home.html")

# About page view
def about(request):
    return render(request, "rulepro/about.html")
