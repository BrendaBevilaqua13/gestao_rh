from django.shortcuts import render

def home_core(request):
    return render(request,'core/index.html')
