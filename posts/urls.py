from django.urls import path

from posts import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('feed', views.feed, name='feed'),
    path('liked', views.show_liked_posts, name='liked_posts'),
    path('new-post/', views.create_post, name='create_post'),
    path('like/', views.post_like, name='post_like'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('search/', views.search, name='search'),
]
