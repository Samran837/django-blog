from django.urls import path
from .import views 
from .views import (PostListView,
                     PostDetailView,
                       PostCreateView,
                         PostUpdateView,
                           PostDeleteView,
                              user_posts
                           )


urlpatterns = [
    path('', views.PostListView.as_view(), name = 'blog-home'),
    path('user/<int:user_id>/', views.user_posts, name = 'user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'blog-post'),
    path('post/new/', views.PostCreateView.as_view(), name = 'blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'blog-post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'blog-post-delete'),
    
    path('about/', views.about, name = 'blog-about')


]
