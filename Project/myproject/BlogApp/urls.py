from django.urls import path
from .views import all_posts, post_details

urlpatterns = [
    path("all_posts/", all_posts,name="all_posts"),
    path("post/<int:pk>/", post_details, name="post_details"),
]