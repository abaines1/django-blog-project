from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post
    
    # Define how you want to grab the list
    # Create the following method that allows us to use Django's ORM
    # Get queryset almost does a sql query on the model
    # Grab the post model and all its objects and then filter based off of published datePostDetailView(DetailView):

    # __lte = less than or equal to
    # filter(published_date__lte=timezone.now().order_by('-published_date'))
    # grab the published dates that are less than or equal to the current time and order them by published date
    # the - in front of ('-published_date') means sort in descending order
    # Django Documentation: https://docs.djangoproject.com/en/5.2/topics/db/queries/

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = Post
    

class CreatePostView(LoginRequiredMixin, CreateView):
    # Login required attributes
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

    model = Post

    # Couple more things we want to accomplish with this view
    # We want only people who are LOGGED IN to have access to creating Posts
    # Mixins are essentially decorators but for CBVs

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'
    
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')