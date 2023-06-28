from django.utils import timezone
from django.shortcuts import render
from .models import Post #.models in this case is same dir or current dir
#not hidden

# Create your views here.
def post_list(request):
    #created vs published not the same, I may have not  added published
    #date to Blog 3
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

