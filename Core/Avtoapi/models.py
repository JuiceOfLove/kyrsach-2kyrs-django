from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_price(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Цена не может быть меньше нуля'),
            params={'value': value})

def validate_likes(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Количесвто лайков не может быть меньше нуля'),
            params={'value': value})



class User(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=25)
    email = models.EmailField(verbose_name='Почта', max_length=40)
    date_of_reg = models.DateField(verbose_name='Дата')
    amount = models.FloatField(verbose_name='Оценка пользователя')
    saler = models.BooleanField(verbose_name='Является продавцом', null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class News(models.Model):
    title = models.CharField(verbose_name='Название объявления', max_length=25)
    text = models.TextField(verbose_name='Текс объявления')
    likes = models.IntegerField(verbose_name='Количество лайков', validators=[validate_likes])
    author = models.ManyToManyField(User, verbose_name='Автор объявления')
    photo = models.FileField(verbose_name='Фото объявления', upload_to="photos")

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Sale(models.Model):
    title = models.CharField(verbose_name='Название поста продажи', max_length=25)
    discription = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена',  null=True , validators=[validate_price])
    saler = models.ManyToManyField(User, verbose_name='Имя продавца')
    photo = models.FileField(verbose_name='Фото автомобиля', upload_to="photos")

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'