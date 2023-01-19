from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'item', views.ItemViewSet)
router.register(r'color', views.ColorViewSet)
router.register(r'status', views.StatusViewSet)

urlpatterns = [
    path('/', include(router.urls))
]
