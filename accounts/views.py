from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

from django.shortcuts import render, redirect
from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def login_view(request):
    title="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #user_qs = user.objects.filter(username=username)
        #if user_qs.count()== 1:
         #   user = user_qs.first()
        login(request,user)
        return redirect("/")
        #redirect

    return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
   # print(request.user.is_authenicated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")

        #return

    context ={
        "form": form,
        "title": title,
    }

    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

