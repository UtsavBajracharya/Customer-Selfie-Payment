from django.shortcuts import render, redirect
from .models import Payment
from fyp.models import Services
from django.contrib import messages
from users.models import AppUser
from django.db.models import Q
from payment.forms import Form, updateForm
from videoTester import VideoCamera
from django.core.paginator import Paginator


# Create your views here.

def pay(request, id):
    if request.method == "POST":
        pay_form = Form(request.POST)
        if pay_form.is_valid():
            payment_amount = (int) (request.POST['payment_amount'])
            appuser = AppUser.objects.get(user=request.user)
            if payment_amount <= appuser.funds:
                if VideoCamera().getFrame():
                    pform = pay_form.save(commit=False)
                    pform.customer = request.user
                    pform.save()
                
                    appuser.funds = appuser.funds - payment_amount
                    appuser.save()
                    messages.success(request, f'Your Payment Was Sucessful!!')
                    return redirect('/home/1')
                else:
                    messages.warning(request, f'face does not match')   
            else:
                messages.warning(request,f'Sorry! You do not have enough balance in your account! Please add funds')
    pay_form = Form()
    context={
        "service": Services.objects.get(services_id=id),
        "pay_form": pay_form
    }
    return render(request, 'payment/pay.html', context)

def view_payments(request, page):
    payments = Payment.objects.filter(customer=request.user)
    paginator = Paginator(payments, 5)
    payments = paginator.get_page(page)
    context ={
        'payments' : payments
    }
    return render(request,'payment/view_payments.html', context)

def search(request):
    get_query = request.POST['q']
    match = Payment.objects.filter(Q(payment_title__icontains=get_query))
    context = {
        "payments": match
    }
    return render(request, 'payment/view_payments.html', context)
    