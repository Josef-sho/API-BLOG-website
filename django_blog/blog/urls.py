from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_posts, name='get_all_posts'),
    path('show_post/<str:post_id>/', views.show_post, name='show_post'),
    path('post/', views.post, name='post'),
    path('edit/<str:post_id>/', views.edit, name='edit'),
    path('delete/<str:post_id>/', views.delete_post, name='delete_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
