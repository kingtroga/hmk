from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from . import models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ForumForm, CommentForm

def index(request):
    query = request.GET.get('query', '')
    forums = models.Forum.objects.all()
    user_is_staff = request.user.is_staff

    if query:
        forums = forums.filter(Q(title__icontains=query) | Q(content__icontains=query))


    paginator = Paginator(forums, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # clean up forum
    for forum in page_obj:
        forum.content = forum.content[0:500] + "..."

    return render(request, 'forum/forum_index.html',
                  {"forums": forums,
                   'query': query,
                   "page_obj": page_obj,
                   'user_is_staff': user_is_staff
                   })


@login_required
def new(request):
    user_is_staff = request.user.is_staff
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.created_by = request.user
            new_forum.save()
            return redirect(f"/embracewellness/forum/detail/{new_forum.id}") #TODO: Redirect to the forum post detail
    else:
        form = ForumForm()
    return render(request, 'forum/forum_new.html',{
        "form": form,
        "user_is_staff": user_is_staff
    })


def detail(request, pk):
    user_is_staff = request.user.is_staff
    forum = get_object_or_404(models.Forum, pk=pk)
    comments = forum.comments.all()
    form = CommentForm()
    more_forums = models.Forum.objects.all().exclude(pk=pk)[0:3]
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.forum = forum
            new_comment.save()
            return redirect(f"/embracewellness/forum/detail/{pk}")
    else:
        form = CommentForm()

    return render(request, 'forum/detail.html', {
        "forum": forum,
        "form": form,
        "comments": comments,
        "more_forums": more_forums,
        'user_is_staff': user_is_staff
    })


