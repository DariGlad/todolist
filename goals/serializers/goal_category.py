from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import GoalCategory


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_field = ('id', 'create', 'updated', 'user')
        fields = '__all__'


class GoalCategorySerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        read_only_field = ('id', 'create', 'updated', 'user')
        fields = '__all__'
