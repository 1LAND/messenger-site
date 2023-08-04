from django.shortcuts import render

from rest_framework.views import APIView



from rest_framework import renderers
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action as a
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import UserSerializer,UserMessageSerializer,UserGroupSerializer

from User.models import User
from UserGroups.models import UserGroups
from UserMessages.models import UserMessages


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class PNGRenderer(renderers.BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data



class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [IsAuthenticated]
    @a(methods=['get'],detail=True)
    def groups(self,request,pk=None):
        user = User.objects.get(pk=pk)
        if request.user.id == int(pk) or bool(request.user and request.user.is_staff):
            return Response({'groups':user.groups.values()})
        return Response({'error':'No permission'})

class AvatarUserView(APIView):
    renderer_classes = [JPEGRenderer]
    def get(self, request, *args, **kwargs):
        try:
            ava = User.objects.get(pk=self.kwargs['pk']).avatar
            return Response(ava, content_type='image/jpg')
        except Exception as err:
            return Response({'file':'DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)

class AvatarGroupView(APIView):
    renderer_classes = [JPEGRenderer]
    def get(self, request, *args, **kwargs):
        try:
            ava = UserGroups.objects.get(pk=self.kwargs['pk']).avatar
            return Response(ava, content_type='image/jpg')
        except Exception as err:
            return Response({'file':'DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)

class UserGroupsPagination(PageNumberPagination):
    page_size=30
    page_size_query_param = 'page_size'
    max_page_size=1000


class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupSerializer 
    permission_classes = [IsAuthenticated]
    pagination_class = UserGroupsPagination

    @a(methods=['get'],detail=True)
    def messages(self,request,pk=None):
        group = UserGroups.objects.get(pk=pk)
        if group.users.filter(email=request.user):
            return Response({'messages':group.messages.values()})
        return Response({'error':'No permission'})
    @a(methods=['get'],detail=True)
    def names(self,request,pk=None):
        group = UserGroups.objects.get(pk=pk)
        
        group.users
        return Response(group.users.values())
# class UserMessageViewSet(viewsets.ModelViewSet):
#     queryset = UserMessages.objects.all()
#     serializer_class = UserMessageSerializer 