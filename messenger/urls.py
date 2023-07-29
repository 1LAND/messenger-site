from django.contrib import admin
from django.urls import re_path,path,include

from rest_framework import routers

from Drf.views import UserViewSet,UserGroupsViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'groups',UserGroupsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/auth/', include('djoser.urls')), 
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
