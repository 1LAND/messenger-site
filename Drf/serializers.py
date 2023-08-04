from rest_framework import serializers

from User.models import User
from UserGroups.models import UserGroups
from UserMessages.models import UserMessages

from Gallery.models import Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = "__all__"

class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessages
        fields = "__all__"


class ImgSerializer(serializers.ModelSerializer):
    # name =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Image
        fields = "__all__"