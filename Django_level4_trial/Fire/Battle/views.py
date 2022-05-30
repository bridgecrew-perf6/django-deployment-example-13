from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request,"Battle/Home.html")

def Testing(request):
    return render(request,"Battle/Testing.html")
def Relative(request):
    return render(request,"Battle/Relative.html")
