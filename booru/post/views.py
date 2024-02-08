from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
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
        if request.user.is_authenticated:
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        return context
