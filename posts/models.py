from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls.base import reverse_lazy
from django.utils import timezone
from unidecode import unidecode


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    slug = models.SlugField(verbose_name='Семантический URL', unique=True)
    body = models.TextField(verbose_name='Тело публикации')
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания', editable=False)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования')
    is_active = models.BooleanField(verbose_name='Отображать', default=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):

        if not self.id:
            self.created_at = timezone.localtime(timezone.now())

        if not self.slug:
            slugy_date = datetime.strftime(
                self.created_at, "-%Y-%m-%d-%H%M%S")
            raw_slug = unidecode(self.title) + slugy_date
            self.slug = slugify(raw_slug)
        self.updated_at = timezone.localtime(timezone.now())

        return super().save(*args, **kwargs)
