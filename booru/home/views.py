from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class MainView(View):
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)