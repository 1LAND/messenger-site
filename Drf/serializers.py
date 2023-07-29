from rest_framework import serializers

from User.models import User
from UserGroups.models import UserGroups,AdminUserGroup
from UserMessages.models import UserMessages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = "__all__"

class AdminUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUserGroup
        fields = "__all__"

class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessages
        fields = "__all__"
