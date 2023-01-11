
from django.utils import timezone

from django.db import models


from django.contrib.auth.models import User

from websource import settings


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    upload_file = models.FileField('Файл на загрузку', blank=True, upload_to="files/%Y/%m/%d/")
    is_published = models.BooleanField('Публикация', default=True)



    def __str__(self):
        return f'Документ: {self.title} - {self.date}'

    def get_absolute_url(self):
        return f'/docs/{self.id}'

    class Meta:
        # swappable = 'user'
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-date', 'title']


class Informed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_informed', on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.DO_NOTHING, db_index=True)
    status_informed = models.BooleanField('Ознакомлен', default=False)
    date_informed = models.DateTimeField('Дата ознакомления', default=timezone.now)
    users_informed = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='title_informed', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/home/{self.id}'

    class Meta:
        verbose_name = 'Ознакомлен(а)'
        verbose_name_plural = 'Ознакомлены'
        # ordering = ['-date', 'title']