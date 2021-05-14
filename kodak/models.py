from django.db import models


class OrderModel(models.Model):
    service = models.CharField('Сервис', max_length=100, blank=True)
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    mail = models.EmailField('Почта')
    comments = models.TextField('Коментарий')
    created = models.DateTimeField('Дата объявления', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)
    photo_file = models.FileField('Изображение', upload_to='photo_file/', blank=True, null=True)
    document_file = models.FileField('Файл', upload_to='document_file/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class MailModel(models.Model):
    mail = models.EmailField('Почта')
    created = models.DateTimeField('Дата объявления', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    def __str__(self):
        return f'{self.mail}'

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'Почты'
