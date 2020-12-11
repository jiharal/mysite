from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('', views.CommentsAPI.get_all, name="list")
]
