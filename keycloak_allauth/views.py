from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import render


def index(request):
    print(request.user.username)
    return render(request, 'index.html')


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def secure_test_one(request):
    return render(request, 'first_secure.html',
                  {'user': request.user.username})


@login_required
def secure_test_two(request):
    return render(request, 'second_secure.html')
