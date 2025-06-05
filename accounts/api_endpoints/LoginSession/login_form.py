from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from accounts.models import User


def login_form(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print('>>>', email, password)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')

        user = authenticate(request, email=email, password=password)
        print('>>>', email, password)


        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Your account is inactive')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')

