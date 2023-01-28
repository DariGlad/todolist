from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import Goal, BoardParticipant


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('не разрешено создавать цель в удалённой категории')
        if not BoardParticipant.objects.filter(
                board_id=value.board_id,
                role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
                user=self.context["request"].user
        ).exists():
            raise serializers.ValidationError('создавать могут только владелец и редакторы')

        return value


class GoalSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('не разрешено изменять цель в удалённой категории')
        if self.instance.category.board_id != value.board_id:
            raise serializers.ValidationError('изменения могут вносить только владелец и редакторы')
        return value
