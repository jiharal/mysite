from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
  path('', views.StoreAPI.get_all, name='all'),
  path('detail/<id>', views.StoreAPI.get_detail, name='detail')
]
