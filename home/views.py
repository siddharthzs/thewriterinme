from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Posts
# Create your views here.

class PostListView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'home/index.html'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'home/viewpost.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['title','img','content', 'tags']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posts
    fields = ['title','img','content', 'tags']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



 

