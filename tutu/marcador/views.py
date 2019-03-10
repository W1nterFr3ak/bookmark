'''
author: Cyber6
version: django 2.x
'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .forms import BookmarkForm
from .models import Bookmark
def bookmark_list(request):
    bookmark = Bookmark.public.all()
    context = {
        'bookmark':bookmark,
    }
    return render(request, 'marcador/bookmark_list.html', context)




def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    context = {'bookmarks': bookmarks, 'owner': user}
    return render(request, 'marcador/bookmark_user.html', context)



@login_required
def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.owner = request.user
            bookmark.save()
            form.save_m2m()
            return redirect('marcador_bookmark_user',
                username=request.user.username)
    else:
        form = BookmarkForm()
    context = {'form': form, 'create': True}
    return render(request, 'marcador/form.html', context)
