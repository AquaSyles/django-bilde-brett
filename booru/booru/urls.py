from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('post/', include('post.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)