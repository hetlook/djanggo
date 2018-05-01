from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login_handle/$', views.login_handle),
    url(r'^info/$', views.user_center_info),
    url(r'^site/$', views.user_center_site),
    url(r'^order/$', views.user_center_order),
]
