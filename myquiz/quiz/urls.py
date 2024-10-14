from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.qpage, name='index'),
    # re_path(r'^register/$', views.register, name='register'),  # This might be unnecessary now
    re_path(r'^login/$', views.login_view, name='login'),
    path('', views.qpage, name='questions'),  
]
