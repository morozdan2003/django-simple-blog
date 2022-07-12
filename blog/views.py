from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

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
    if Post.objects.count() == 0:
        return HttpResponse("This blog is empty")
    else:
        posts_list = Post.objects.order_by("-posted_at")
        context = {'posts_list': posts_list}
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
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.contents = request.POST['contents']
        new_post.posted_at = timezone.now()
        new_post.save()
        return HttpResponse('Posted successfully! <a href="/">Go to home.</a>')
    else:
        return render(request, 'blog/PostWrite.html', {})