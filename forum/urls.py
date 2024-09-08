from django.urls import path
from forum_project import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('thread/add/', views.add_thread, name='add_thread'),
    path('thread/<int:pk>/add_post/', views.add_post, name='add_post'),
]
