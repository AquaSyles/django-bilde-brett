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
        queryset = super().get_queryset()
        tags_param = self.request.GET.get('tags')
        
        if tags_param:
            if tags_param == 'all':
                return queryset.order_by('-posted_date')  # Return all posts if 'all' is provided
            
            # Split the search tags by spaces
            search_tags = tags_param.split()

            print(search_tags)

            # Initialize a Q object to build the query dynamically
            q_object = Q()

            # Iterate over each search tag
            for tag in search_tags:
                if tag.startswith('-'):
                    # Exclude posts with the tag if it's a blacklist tag
                    q_object &= ~(
                        Q(tags__startswith=tag[1:]) |
                        Q(tags__contains=' ' + tag[1:] + ' ') |
                        Q(tags__endswith=tag[1:])
                    )
                else:
                    # Include posts with the tag
                    q_object &= (
                        Q(tags__startswith=tag) |
                        Q(tags__contains=' ' + tag + ' ') |
                        Q(tags__endswith=tag)
                    )

            # Filter the queryset based on the constructed Q object
            queryset = queryset.filter(q_object)

        return queryset.order_by('-posted_date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        return context
