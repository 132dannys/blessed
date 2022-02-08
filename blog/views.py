from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView


def blog_home(request):
    posts = Post.objects.order_by('title')
    return render(request, 'blog/blog_home.html', {'posts': posts}, )


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/details_view.html'
    context_object_name = 'article'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create.html'

    form_class = PostForm


class BlogDeleteView(DeleteView):
    model = Post
    success_url = '/blog'
    template_name = 'blog/blog-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        else:
            error = 'Форма была неверной'
    form = PostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', data)
