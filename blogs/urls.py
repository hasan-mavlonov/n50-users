from django.urls import path
from blogs.views import users, blogs

app_name = 'blogs'
urlpatterns = [
    path('users/', users.user_list_create, name='user_list_create'),
    path('users/<int:pk>', users.user_detail, name='user_detail'),
    path('blogs/', blogs.blog_list_create, name='blog_list_create'),
    path('blogs/<int:pk>', blogs.blog_detail, name='blog_detail'),
    # In urls.py
    path('blogs/users/<int:user_id>', blogs.blog_list_of_user, name='blog-list-of-user')
]