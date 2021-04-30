from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

from messenger.models import Messenger

# Create your views here.
def login(request):
    if request.method=='POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Log In Sucessful')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Details')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        # Get form values
        fname =  request.POST['first_name']
        lname =  request.POST['last_name']
        user_name =  request.POST['username']
        email =  request.POST['email']
        pass1 =  request.POST['password']
        pass2 =  request.POST['password2']
    

        # Check if password match
        if pass1 == pass2:
            # Check username
            if User.objects.filter(username=user_name).exists():
                messages.error(request,'User Name Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email Taken Already')
                    return redirect('register')
                else:
                    #Give an entry
                    user = User.objects.create_user(username=user_name,password=pass1,email=email,first_name=fname,last_name=lname)
                    user.save();
                    messages.success(request,'Registered Sucessfully')
                    return redirect('login')
        else:
            messages.error(request,'Password Not Matched')
            return redirect('register')

        messages.error(request,'Testing Error')
        return redirect('register')
    else:
	    return render(request,'accounts/register.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'Log Out Sucessful')
        return redirect('index')

def dashboard(request):
    user_data = Messenger.objects.order_by('-contact_data').filter(user_id=request.user.id)
    
    context = {
        'data' : user_data
    }

    return render(request,'accounts/dashboard.html',context)
