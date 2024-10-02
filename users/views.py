from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.form import RegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            return redirect(reverse_lazy('users:login'))
        else:
            errors = form.errors
            return render(request, 'registrations/register.html', {'errors': errors})
    else:
        return render(request, 'registrations/register.html')


def login_view(request):
    return render(request, 'registrations/login.html')


def logout_view(request):
    return HttpResponse('Logged out successfully.')