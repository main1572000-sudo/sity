from django.shortcuts import render
from .forms import MemberLogin
from .models import Member
# Create your views here.
def mainy(request):
    return render(request,'main.html')

def abouty(request):
    return render(request,'about.html')

def formy(request):
    if request.method == 'POST':
        MemberLogin(request.POST).save()
        
    return render(request,'formy.html',{'ml':MemberLogin})

def signy(request):
    
    return render(request,'signy.html',{'data':Member.objects.all()})
#......................................
