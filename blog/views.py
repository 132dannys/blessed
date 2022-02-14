from django.http import HttpResponse, HttpResponseRedirect
from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView


class BlogHome(TemplateView):
    template_name = 'blog/blog_home.html' 

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('title')
                
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details_view.html'
    context_object_name = 'article'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create.html'

    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog'
    template_name = 'blog/blog_delete.html'


class Create(View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name ='blog/create.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')     
        return render(request, self.template_name, {'form': form})