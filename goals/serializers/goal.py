from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import Goal


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Goal
        read_only_field = ('id', 'create', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('не разрешено создавать цель в удалённой категории')
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('не являетесь владельцем категории')
        return value


class GoalSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = Goal
        read_only_field = ('id', 'create', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('не являетесь владельцем категории')
        return value
