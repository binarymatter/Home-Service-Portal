from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.http import JsonResponse

from .forms import ContactModelForm

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'baseapp/index.html')

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password error!')
            
    context = {}
    return render(request,'baseapp/log-in.html',context)


def logoutfunc(request):
    logout(request)
    return redirect('loginpage')


def signup(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user )
            return redirect('loginpage')



    context = {'form':form}
    return render(request,'baseapp/sign-up.html',context)


def pestcontrol(request):
    return render(request,'baseapp/pest.html')




def bookingforpest(request):
    form = ContactModelForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'baseapp/pest-contact.html', {'form': form})