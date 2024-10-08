from django.db import models

# Create your models here.

# menu_app/models.py

from django.urls import reverse

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родитель")
    url = models.CharField(max_length=255, blank=True, verbose_name="URL")
    named_url = models.CharField(max_length=255, blank=True, verbose_name="Named URL")
    menu_name = models.CharField(max_length=50, verbose_name="Название меню")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
