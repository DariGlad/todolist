from django.db import models


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now_add=True)


class GoalCategory(DatesModelMixin):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    title = models.CharField(verbose_name='название', max_length=255)
    user = models.ForeignKey('core.User', verbose_name='автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='удалена', default=False)

    def __str__(self):
        return self.title


class Goal(DatesModelMixin):
    class Meta:
        verbose_name = 'цель'
        verbose_name_plural = 'цели'

    class Status(models.IntegerChoices):
        to_do = 1, 'к выполнению'
        in_progress = 2, 'в процессе'
        done = 3, 'выполнено'
        archived = 4, 'архив'

    class Priority(models.IntegerChoices):
        low = 1, 'низкий'
        medium = 2, 'средний'
        high = 3, 'высокий'
        critical = 4, 'критический'

    user = models.ForeignKey(
        'core.User',
        verbose_name='пользователь',
        related_name='goals',
        on_delete=models.PROTECT,
    )
    category = models.ForeignKey(
        'goals.GoalCategory',
        verbose_name='категория',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='заголовок',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        null=True,
        blank=True,
        default=None,
    )
    due_date = models.DateField(
        verbose_name='дата выполнения',
        null=True,
        blank=True,
        default=None,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='статус',
        choices=Status.choices,
        default=Status.to_do,
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='приоритет',
        choices=Priority.choices,
        default=Priority.medium,
    )

    def __str__(self):
        return self.title


class GoalComment(DatesModelMixin):
    class Meta:
        verbose_name = 'комментарий к цели'
        verbose_name_plural = 'комментарии к цели'

    user = models.ForeignKey(
        'core.User',
        verbose_name='автор',
        related_name='goal_comments',
        on_delete=models.PROTECT,
    )
    goal = models.ForeignKey(
        'goals.Goal',
        verbose_name='цель',
        related_name='goal_comments',
        on_delete=models.PROTECT,
    )
    text = models.TextField(verbose_name='текст')
