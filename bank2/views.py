import time
import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from bank2.forms import userform,loginf,transfer
from .models import acc,transcation
from django.core.exceptions import ObjectDoesNotExist


def account(request):
    rn=random.randint(1000000000,9999999999)
    return HttpResponse(f"<h1>{rn}</h1><br><h1>copy the number then move to paste it on account number field</h1>")
acno=[]
def home(request):
    return render(request,'base.html')
def create(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        return render(request,'register.html',{'form':form})



def login(request):
    form=loginf()
    if request.method=='POST':
        form=loginf(request.POST)
        if form.is_valid():
            phone=form.cleaned_data.get('phone')
            user=acc.objects.filter(phone=phone).first()
            if user is not None:
                request.session['user_id'] = user.pk

                return render(request,'frame.html',{'user':user})
            else:
                return render(request,'notfound.html',{'data':'acc not fount'})

    else:
        # form=loginf()
        return render(request,'login.html',{'form':form})

def details(request):
    user_id=request.session.get('user_id')
    user=acc.objects.get(pk=user_id)

    return render(request,'details.html',{'user':user})
def withdraw(request):
    form=transfer()
    user_id=request.session.get('user_id')
    data=acc.objects.get(pk=user_id)
    sender=data.phone
    if request.method=='POST':
        form=transfer(request.POST)
        if form.is_valid():
            # sender=form.cleaned_data.get('sender')
            reciver=form.cleaned_data.get('reciver')
            amount=form.cleaned_data.get('amount')
            try:
                s=acc.objects.get(phone=sender)
                r=acc.objects.get(phone=reciver)
                pres=s.amount
                prer=r.amount

                if (s is not None) and (r is not None):
                    if s.amount>=amount:
                        s.amount=s.amount-amount
                        r.amount=r.amount+amount
                        s.save()
                        r.save()
                        t=transcation(from_phone=sender,to_phone=reciver,t_amount=amount,dt=datetime.datetime.now(),p_amount=pres,total=s.amount)
                        t1=transcation(from_phone=reciver,to_phone=sender,t_amount=amount,dt=datetime.datetime.now(),p_amount=prer,total=r.amount)
                        t1.save()
                        t.save()

                        return redirect('details')
                    else:
                        return render(request,'notfound.html',{'data':'insufficient balances'})
            except ObjectDoesNotExist:

                return render(request,'notfound.html',{'data':'acc not found'})

    else:
        return render(request,'transfer.html',{'form':form})


def statement(request):

    db=request.session.get('user_id')
    data=acc.objects.all().get(pk=db)
    phone=data.phone

    try:
        t=transcation.objects.filter(from_phone=phone)


        if t is not None:
            return render(request,'history.html',{'data':t,'phone':phone})


    except ObjectDoesNotExist:
        return render(request, 'notfound.html', {'data': 'not found'})


    return render(request,'login.html',{'form':form})


