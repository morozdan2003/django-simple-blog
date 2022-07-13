from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import forms, models, settings

base_context = {
    'offline_bootstrap': settings.USE_OFFLINE_BOOTSTRAP,
    'online_bootstrap_location': settings.ONLINE_BOOTSTRAP_LOCATION,
    'offline_bootstrap_location': settings.OFFLINE_BOOTSTRAP_LOCATION,
}

# Posts' list view
def PostList(request):
    context = base_context
    context['posts_list'] = models.Post.objects.order_by("-posted_at")
    context['posts_count'] = models.Post.objects.count()
    #context = {'posts_list': models.Post.objects.order_by("-posted_at"), 'posts_count': models.Post.objects.count()}
    return render(request, 'blog/PostList.html', context)

# Post viewing view 
def PostView(request):
    try:
        context = base_context
        context['post'] = models.Post.objects.get(pk=request.GET.get('post'))
        return render(request, 'blog/PostView.html', context)
    except Post.DoesNotExist:
        raise Http404()

# Post writing view
def PostWrite(request):
    context = base_context
    if request.method == "POST":
        form = forms.PostWriteForm(request.POST)
        if form.is_valid():
            post = models.Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.posted_at = timezone.now()
            post.save()
            return render(request, 'blog/PostWriteSuccess.html', context)
    else:
        form = forms.PostWriteForm()
    context['form'] = form
    return render(request, 'blog/PostWrite.html', context)