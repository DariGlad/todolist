from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import GoalComment


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = GoalComment
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_goal(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('не являетесь владельцем цели')
        return value


class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = GoalComment
        read_only_fields = ('id', 'created', 'updated', 'user', 'goal')
        fields = '__all__'

    def validate_goal(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('не являетесь владельцем цели')
        return value
