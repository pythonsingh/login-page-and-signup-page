from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def disp_view(request):
    return render(request,'index.html')

def disp_view1(request):
    return render(request,'signup.html')
