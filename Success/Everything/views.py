from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"Everything/HomePage.html")

def Other(request):
    return render(request,"Everything/Other.html")

def Relative(request):
    return render(request,"Everything/relative.html")
