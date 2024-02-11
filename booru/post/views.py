from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

from django.db.models import Q

NUM_POSTS = 12

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
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    paginate_by = NUM_POSTS

    def get_queryset(self):
        # Ordered object of all posts
        queryset = super().get_queryset().order_by('-posted_date')
        tags_param = self.request.GET.get('tags')
        
        # Returns all images if no search tags or if the user searched using the all tag
        if tags_param and tags_param != 'all':

            return self.filter_posts_by_tags(queryset, tags_param)

        return queryset


    def filter_posts_by_tags(self, queryset, tags_param):
        search_tags = self.parse_tags_param(tags_param)
        filtered_posts = []

        for post in queryset:
            post_tags = set(post.tags.split())
            if self.post_contains_tags(post_tags, search_tags):
                filtered_posts.append(post)

        return filtered_posts

    def parse_tags_param(self, tags_param):
        search_tags = tags_param.split()
        include_tags = set()
        exclude_tags = set()

        for tag in search_tags:
            if tag.startswith('-'):
                exclude_tags.add(tag[1:])
            else:
                include_tags.add(tag)

        return include_tags, exclude_tags

    def post_contains_tags(self, post_tags, search_tags):
        include_tags, exclude_tags = search_tags
        return include_tags.issubset(post_tags) and not any(tag in post_tags for tag in exclude_tags)




class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        return context
