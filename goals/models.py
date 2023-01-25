from django.db import models

class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now_add=True)

class GoalCategory(DatesModelMixin):
    class Meta:
        verbose_name='категория'
        verbose_name_plural='категории'

    title = models.CharField(verbose_name='название', max_length=255)
    user = models.ForeignKey('core.User', verbose_name='автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='удалена', default=False)

    def __str__(self):
        return self.title


