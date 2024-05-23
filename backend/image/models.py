from django.db import models


class ImagesModel(models.Model):
    """Model for 'Images' page."""

    id = models.AutoField(
        primary_key=True,
        unique=True
    )
    image = models.TextField(
        verbose_name="Картинка",
        help_text="Добавьте картинку",
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=250,
        blank=True,
        help_text="Введите описание",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Картинки"
        verbose_name_plural = "Картинки"
