from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from.models import Profile
def base(request):
    return render(request,'myapp/base.html')
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            photo = form.cleaned_data.get('photo')
            Profile.objects.create(user=user, photo=photo)

            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'myapp/register.html', {'form': form})




