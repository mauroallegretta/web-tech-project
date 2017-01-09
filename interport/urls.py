from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^user_profile/(?P<pk>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register_user$', views.register_user, name='register_user'),
    url(r'^user_list$', views.user_list, name='user_list'),
    url(r'^person_list$', views.person_list, name='person_list'),
    url(r'^future/$', views.future, name='future'),
    url(r'^author/$', views.author, name='author'),
    url(r'^idea/$', views.idea, name='idea'),
    url(r'^$', views.home, name='home'),
]



"""
    url(r'^carousel_creator/$', views.carousel_creator, name='carousel_creator'),
    url(r'^user_carousel/(?P<pk>[0-9]+)/$', views.user_carousel, name='user_carousel'),

"""