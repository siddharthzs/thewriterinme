from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    PostListView, PostDetailView, PostUpdateView,
    PostCreateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='blog-viewpost'),
    path('post/new/',PostCreateView.as_view(),name='blog-newpost'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='blog-editpost'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='blog-deletepost'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
