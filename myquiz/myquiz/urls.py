from django.urls import path, re_path, include
from django.contrib import admin
from myquiz import views as index_views
from rest_framework.urlpatterns import format_suffix_patterns
from quizapi import views

urlpatterns = [
    re_path(r'^$', index_views.index, name='index'),
    re_path(r'^login/$', index_views.login, name='login'),
    re_path(r'^register/$', index_views.register, name='register'),  # Use index_views for register
    re_path(r'^questions/', include('quiz.urls')),
    re_path(r'^quizapi/', views.QuizApiList.as_view(), name='quizapi'),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
