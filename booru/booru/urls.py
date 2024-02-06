from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('post/', include('post.urls')),
]
