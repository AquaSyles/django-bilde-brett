from django.urls import path, include
from .views import UploadFileView, PostListView
app_name = 'post'

# Define your URL patterns
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('', PostListView.as_view(), name='post_list'),
]

from django.conf import settings
from django.conf.urls.static import static

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)