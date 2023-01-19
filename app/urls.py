from django.urls import path, include
from rest_framework import routers

# from app import views

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'item', views.ItemViewSet)

urlpatterns = [
    path('/', include(router.urls))
]
