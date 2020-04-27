# -*- coding:utf-8 -*-
from django.conf.urls import url

from ranking_list import views

urlpatterns = [
        url(r'ranking_list_search/', views.ranking_list_search),
        url(r'post_grade/', views.post_grade)
]
