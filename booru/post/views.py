from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

class UploadFileView(FormView):
    template_name = 'post/upload_file.html'
    form_class = PostForm
    success_url = '/post/'  # Change this to the appropriate URL

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:main')
            
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Create this template
    context_object_name = 'posts'
    ordering = ['-posted_date']