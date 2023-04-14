from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comments
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required


# It shows all posts. Available to everyone.
class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'post_list.html'
    context_object_name = 'posts'


# It shows one post. Available to everyone.
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        return context


# View, that use Form for creating the NewPost. Available to logged-in users.
# Add settings post_author!
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


# View, that use Form for editing post. Available to logged-in users.
# Add settings post_author!
class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'


# View for deleting posts. Available for author and admin.
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


# List of messages. Available for author.
class CommentsList(ListView):
    model = Comments
    ordering = '-time_in'
    template_name = 'comments_list.html'
    context_object_name = 'com'


class CommentDetail(DetailView):
    model = Comments
    template_name = 'comment_detail.html'
    context_object_name = 'com'


# Available for logged-in person.
def create_comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.com_author = request.user
            p = Post.objects.get(id=pk)
            instance.com_post = p
            instance.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'comment_send.html', {'form': form})


class CommentDelete(DeleteView):
    model = Comments
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('comments')


def accept_comment(request, pk):
    instance = Comments.objects.get(id=pk)
    post_id = instance.com_post.id
    instance.com_accept = True
    instance.save()
    return redirect(f'/{post_id}')
