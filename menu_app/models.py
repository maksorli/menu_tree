from django.db import models

# Create your models here.
 
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название меню")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название пункта")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, verbose_name="Слаг")
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name="Родитель"
    )
    url = models.CharField(max_length=255, blank=True, verbose_name="URL")
    named_url = models.CharField(max_length=255, blank=True, verbose_name="Named URL")
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="Меню", 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            if self.named_url:
                return reverse(self.named_url)
            elif self.url:
                return self.url
            else:
                return reverse('menu_item', kwargs={'slug': self.slug})
        except Exception as e:
            print(f"Error in get_absolute_url for item {self.name}: {e}")
            return '#'