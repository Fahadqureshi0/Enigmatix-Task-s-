from django.contrib import admin #type:ignore
from django.urls import path, include #type:ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TodoApp.urls')),
    path('', include("BlogApp.urls")),
    path('', include("myapp.urls")),
]