from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sign-up$', views.SignUp.as_view(), name='sign-up'),
    url(r'^$', views.index, name='index'),
    url(r'^game/$', views.game, name='game'),
    url(r'^dashboard/$', views.UserList.as_view(), name='dashboard'),
    url(r'^score/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='score'),
    url(r'^score/(?P<id>[0-9]+)/update/(?P<newscore>[0-9]+)$', views.UserDetail_update, name='update'),
]
