from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'index/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^select$', views.select_user_type, name='select_user_type'),
    url(r'^want_reader/(?P<user_id>[0-9]+)$', views.want_reader, name='want_reader'),
    url(r'^want_reader/save/(?P<text_id>[0-9]+)$', views.want_reader_save_answer, name='want_reader_save_answer'),
    url(r'^want_writer$', views.want_writer, name='want_writer'),

]
