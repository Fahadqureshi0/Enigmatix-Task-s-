from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogModel


# All Blog Posts______!
def all_posts(request):
    posts = BlogModel.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "BlogApp/all_posts.html", { "page_obj": page_obj })



# Posts Details_______!
def post_details(request, pk):
    post = get_object_or_404(BlogModel, pk=pk)
    return render(request, "BlogApp/post_details.html", {"post": post})



