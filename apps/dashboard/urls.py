#dashboard
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register', views.registration, name='registration'),
    url(r'^sign_in', views.sign_in, name='sign_in'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'^hide', views.hide, name='hide'),
    url(r'^users/new', views.new_user, name='new_user'),
    url(r'^users/add', views.add_user, name='add_user'),
    url(r'^users/edit/(?P<id>\d+)/$', views.edit_admin, name='edit_admin'),
    url(r'^users/edit/info/(?P<id>\d+)/$', views.edit_info, name='edit_info'),
    url(r'^users/edit/password/(?P<id>\d+)/$', views.edit_password, name='edit_password'),
    url(r'^users/edit', views.profile, name='profile'),
    url(r'^users/edit/description/(?P<id>\d+)/$', views.edit_description, name='edit_description'),
    url(r'^users/show/(?P<id>\d+)/$', views.show_user, name='show_user'),
    url(r'^message/(?P<owner_id>\w+)*$', views.message, name='message'),
    url(r'^comment/(?P<owner_id>\w+)*/(?P<message_id>\d+)*$', views.comment, name='comment'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
]
