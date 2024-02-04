from django.urls import path, include
from .views import MainView

app_name = 'home'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]