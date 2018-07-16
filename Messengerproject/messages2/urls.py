from django.urls import path
from .import views
from django.urls import include, re_path

app_name='messages2'

urlpatterns = [
    path('', views.message_featured, name="list"),
    path('create/', views.message_create, name="create"),
    path('sent/', views.message_sent, name="sent"),
    
    re_path('(?P<slug>[\w-]+)/$', views.message_detail, name="detail"),
]