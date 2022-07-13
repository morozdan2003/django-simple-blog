from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from .forms import PostWriteForm

# Blog's index page view (static)
def BlogIndexPage(request):
    response = HttpResponse("""
    <html>
        <head>
            <title>Homepage</title>
        </head>
        <body>
            <h1>Welcome to Blog app</h1>
            <p>Please select the action:</p>
            <ul>
                <li><a href="list/">See a post list</a></li>
                <li><a href="write/">Write a new post</a></li>
            </ul>
        </body>
    </html>
    """)
    return response

# Posts' list view
def PostList(request):
    context = {'posts_list': Post.objects.order_by("-posted_at"), 'posts_count': Post.objects.count()}
    return render(request, 'blog/PostList.html', context)

# Post viewing view 
def PostView(request):
    try:
        post_object = Post.objects.get(pk=request.GET.get('post'))
        context = {'post': post_object}
        return render(request, 'blog/PostView.html', context)
    except Post.DoesNotExist:
        raise Http404()

# Post writing view
def PostWrite(request):
    if request.method == "POST":
        form = PostWriteForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.posted_at = timezone.now()
            post.save()
            return render(request, 'blog/PostWriteSuccess.html',{})
    else:
        form = PostWriteForm()
    return render(request, 'blog/PostWrite.html', {'form': form})