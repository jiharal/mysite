from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'MySite Admin'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('store/', include('store.urls')),
    path('comments/', include('comments.urls')),
]
