from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.order),
    url(r'^handle/$', views.order_handle),
    url(r'^pay/$', views.pay),

]