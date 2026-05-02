from django.shortcuts import render,get_object_or_404
from .forms import MemberLogin
from .models import Member,Product
# Create your views here.
def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def mainy(request):
    return render(request,'main.html')

def shop(request):
    return render(request,'shop.html',{'product':Product.objects.all()})

def formy(request):
    if request.method == 'POST':
        MemberLogin(request.POST).save()
        
    return render(request,'formy.html',{'ml':MemberLogin})

def signy(request):
    
    return render(request,'signy.html',{'data':Member.objects.all()})

def info(request,pk):
    data = get_object_or_404(Member, pk=pk)
    
    return render(request, 'info.html', {'data': data})
#......................................
