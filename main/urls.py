from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('newpost', views.newpost, name="newpost"),
    path('intro', views.intro, name="intro"),
    path('postlist', views.postlist, name="postlist"),
    path('post/postlist', views.re_post, name="re_post"),
    path('post/newpost', views.newpost, name="post_newpost"),
    path('post/<int:post_id>', views.post, name="post"),
    path('post/postlike', views.postlike, name="postlike"),
    path('post/accounts/login', views.jump_login, name="re_login"),
    path('post/accounts/register', views.jump_register, name="re_register"),
    path('post/accounts/logout', views.jump_logout, name="re_logout")
]
