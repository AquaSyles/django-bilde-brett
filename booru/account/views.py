from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

class AccountView(View):
    template_name = 'account/index.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')

        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home:main'))  # Redirect to the main view in the 'home' app
        else:
            # Add logic for unsuccessful login attempt (e.g., display an error message)
            pass

        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home:main'))  # Redirect to the main view in the 'home' app

class SignupView(View):
    template_name = 'account/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # Log the user in after signup
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home:main'))  # Redirect to the main view in the 'home' app
            else:
                # Handle the case where authentication fails after signup
                return HttpResponseRedirect(reverse('home:main'))

        return render(request, self.template_name, {'form': form})
