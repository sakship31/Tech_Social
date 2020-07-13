from django.conf.urls import url
from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
    url(r"new/in/(?P<pk>\d+)/$", views.CreatePost.as_view(), name="create1"),
    url(r"comment/in/(?P<pk>\d+)/$", views.CreateComment.as_view(), name="create2"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    url(r"comment/delete/(?P<pk>\d+)/$",views.DeleteComment.as_view(),name="delete1"),
]
