from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 방명록 목록을 보여주는 URL
    path('add/', views.add_entry, name='add_entry'),  # 방명록 항목 추가 페이지 URL
]
