from django.shortcuts import render,get_object_or_404
from django.http import *
from mygarments.models import FormalShirt,Signup
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.mail import send_mail



def base(request):
    lst=FormalShirt.objects.all()
    return render(request,'base.html',{'lst':lst})
def aboutus(request):
    return render(request,'aboutus.html')
def searchlist(request):
    str=request.GET.get('query')
    if str:
        match1=FormalShirt.objects.filter(Q(name__icontains=str)|Q(description__icontains=str))
        if match1:
            return render(request,'searchlist.html',{'match1':match1})
        else:
            messages.error(request,'no result found')
    else:
        messages.error(request, 'enter any data')
    return render(request,'searchlist.html')

def formalshirtslist(request):
    lst = FormalShirt.objects.all()
    return render(request,'formalshirtslist.html',{'lst':lst})

def regprocessview(request):
    v1=request.GET.get('n1')
    v2=request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    obj=Signup(fullname=v1,userid=v2,password=v3,address=v4)
    obj.save()
    msg=v1+' Registration done successfully'
    return render(request,'base.html',{'msg':msg})
def loginprocessview(request):
    try:
        v1 = request.GET.get('n1')
        v2 = request.GET.get('n2')
        obj=Signup.objects.get(userid=v1)
        if obj.userid==v1 and obj.password==v2:
            msg=v1+' login successfully'

            return render(request, 'base.html',{'msg':msg})
        else:
            msg = v1 + ' login failure'
            return render(request,'base.html',{'msg':msg})
    except ObjectDoesNotExist:
        msg = v1 + ' login failure'
        return render(request,'base.html',{'msg':msg})
def productitem(request,x):
    lst=FormalShirt.objects.get(Q(id__icontains=x))
    return render(request,'product.html',{'lst':lst})
list=[]
price=[]
def cart(request,x):
    item=FormalShirt.objects.get(id=x)
    list.append(item)
    price.append(item.price)
    total=sum(price)
    return render(request,'cart.html',{'list':list},{'total':total})


def gmail(request):
    return render(request,'gmailhome.html')