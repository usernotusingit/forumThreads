from django.shortcuts import render, redirect, get_object_or_404
from forum.models import Thread, Post
from django.contrib.auth.decorators import login_required
from forum.forms import ThreadForm, PostForm

# List all threads
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'forum/thread_list.html', {'threads': threads})

# View a single thread and its posts
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = thread.posts.all()
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})

# Add a new thread
@login_required
def add_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user
            thread.save()
            return redirect('thread_detail', pk=thread.pk)
    else:
        form = ThreadForm()
    return render(request, 'forum/add_thread.html', {'form': form})

# Add a post to a thread
@login_required
def add_post(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('thread_detail', pk=thread.pk)
    else:
        form = PostForm()
    return render(request, 'forum/add_post.html', {'form': form, 'thread': thread})
