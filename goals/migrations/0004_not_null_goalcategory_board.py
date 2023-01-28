# Generated by Django 4.1.5 on 2023-01-27 13:51

from django.db import migrations, transaction
from django.utils import timezone


def create_objects(apps, schema_editor):
    User = apps.get_model("core", "User")
    Board = apps.get_model("goals", "Board")
    BoardParticipant = apps.get_model("goals", "BoardParticipant")
    GoalCategory = apps.get_model("goals", "GoalCategory")

    with transaction.atomic():  # Применяем все изменения одной транзакцией
        now = timezone.now()
        for user in User.objects.all():  # Для каждого пользователя
            new_board = Board.objects.create(
                title="Мои цели",
                created=now,  # Проставляем вручную по той же причине, что описана вверху
                updated=now
            )
            BoardParticipant.objects.create(
                user=user,
                board=new_board,
                role=1,  # Владелец, проставляем числом, не импортируем код по той же причине
                created=now,
                updated=now
            )

            # проставляем всем категориям пользователя его доску
            GoalCategory.objects.filter(user=user).update(board=new_board)


class Migration(migrations.Migration):
    dependencies = [
        ('goals', '0003_goalcategory_board'),
    ]

    operations = [
        migrations.RunPython(create_objects)
    ]
