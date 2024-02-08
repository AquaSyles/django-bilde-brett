from django.urls import path, include
from .views import UploadFileView, PostListView, PostDetailView
app_name = 'post'

# Define your URL patterns
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]

