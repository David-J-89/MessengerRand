from django.urls import path
from .import views
from django.urls import include, re_path

app_name='messages2'

urlpatterns = [
    path('', views.message_list, name="list"),
    path('create/', views.message_create, name="create"),
    re_path('(?P<slug>[\w-]+)/$', views.message_detail, name="detail"),
]