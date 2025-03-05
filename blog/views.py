from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import BlogForm

def index(request):
    user_is_staff = request.user.is_staff
    query = request.GET.get('query', '')
    blogs = models.Blog.objects.all()

    if query:
        blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))


    paginator = Paginator(blogs, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # clean up forum
    for blog in page_obj:
        blog.content = blog.content[0:500] + "..."

    return render(request, 'blog/blog_index.html',
                  {"blogs": blogs,
                   'query': query,
                   "page_obj": page_obj,
                   'user_is_staff': user_is_staff})

@login_required
def new(request):
    user_is_staff = request.user.is_staff
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect(f"/embracewellness/blog/detail/{new_blog.id}") #TODO: Redirect to the blog post detail
    else:
        form = BlogForm()
    return render(request, 'blog/blog_new.html',{
        "form": form,
        'user_is_staff': user_is_staff
    })

def detail(request, pk):
    user_is_staff = request.user.is_staff
    blog = get_object_or_404(models.Blog, pk=pk)
    more_blogs = models.Blog.objects.all().exclude(pk=pk)[0:3]

    return render(request, 'blog/detail.html', {
        "blog": blog,
        "more_blogs": more_blogs,
        'user_is_staff': user_is_staff
    })

