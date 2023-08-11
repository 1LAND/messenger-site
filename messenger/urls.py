from django.contrib import admin
from django.urls import re_path,path,include

from rest_framework import routers

from Drf.views import UserViewSet,UserGroupsViewSet,AvatarUserView,AvatarGroupView

router = routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'groups',UserGroupsViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/users/<int:pk>/avatars/',AvatarUserView.as_view()),
    path('api/groups/<int:pk>/avatars/',AvatarGroupView.as_view()),
    path('api/auth/', include('djoser.urls')), 
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
