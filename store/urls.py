from django.urls import include, path
from rest_framework import routers

from .views import StoreVieSet

router = routers.DefaultRouter()
router.register(r'store', StoreVieSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
