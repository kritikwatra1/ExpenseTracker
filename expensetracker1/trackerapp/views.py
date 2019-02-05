from django.shortcuts import render
from . import forms
from trackerapp.models import Customer, Wallet, Transaction
from django.http import HttpResponse

def index(request):
    form = forms.LoginForm()
    if request.method == 'POST':

        form = forms.LoginForm(request.POST)

        if form.is_valid():
            try:
                customer_data = Customer.objects.get(emailid=form.cleaned_data['email'])
                print("matched")
                print(customer_data.psswd)
                print(form.cleaned_data['password'])
                if customer_data.psswd == form.cleaned_data['password']:
                    print(customer_data.psswd)
                    print(form.cleaned_data['password'])
                    request.session['emailid'] = form.cleaned_data['email']
                    return render(request, "trackerapp/wallet.html")
                else:
                    render(request, 'trackerapp/index.html', {'loginform':form, 'login': False})
            except RuntimeError:
                return render(request, 'trackerapp/index.html', {'loginform':form, 'login': False})



            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])

    return render(request,'trackerapp/index.html', {'loginform':form, 'login': True})


def wallet(request):
    email_id = request.session['emailid']
    print(email_id)
    customer = Customer.objects.get(emailid = email_id)
    cid = customer.cid
    print(cid)
    wallets = ""
    try:
        wallets = wallets = Wallet.objects.get(cid = cid)
    except:
        return render(request,'trackerapp/wallet.html',{'empty': True})
    return render(request,'trackerapp/wallet.html',{'empty':False, 'wallets': wallets})





def signup(request):
    signupform = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            try:
                customer_data = Customer.objects.get(emailid=form.cleaned_data['Emailid'])
                return render(request, 'trackerapp/signup.html', {'signupform':signupform, 'exists': True})
            except:
                customer = Customer(emailid=form.cleaned_data['Emailid'], psswd=form.cleaned_data['Password'], firstname=form.cleaned_data['Firstname'],lastname = form.cleaned_data['Lastname'] )
                customer.save()
    return render(request,'trackerapp/signup.html', {'signupform':signupform, 'exists': False})
