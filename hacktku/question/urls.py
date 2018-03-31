from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sign-up$', views.SignUp.as_view(), name='sign-up'),
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.UserList.as_view(), name='dashboard'),
]
