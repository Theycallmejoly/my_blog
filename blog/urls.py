from django.urls import path
from . import views
urlpatterns = [
    path("" , views.starting_page , name="starting-page"),
    path("posts" , views.posts , name="post-page"),
    path("post/<slug:slug>" , views.singel_detail, name="post-detail-page") #/post/my-first-post
]
