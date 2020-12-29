from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *


def index(request):
    return render(request, 'gallery/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../home/')
    else:
        form = UserCreationForm()
    return render(request, 'gallery/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('../home/')
            else:
                return redirect('../invalid-login/')
    else:
        form = LoginForm()
    return render(request, 'gallery/login.html', {'form': form})


def invalid_login(request):
    return render(request, 'gallery/invalid_login.html')


def home(request):
    return render(request, 'gallery/home.html')


def book(request):
    context = {}
    form = BookingForm(request.POST or None)

    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('../success/')

    context['form'] = form
    return render(request, 'gallery/book.html', context)


def success(request):
    booking = Booking.objects.filter(user=request.user).latest('booked_at')
    context = {
        'booking': booking
    }
    return render(request, 'gallery/success.html', context)
