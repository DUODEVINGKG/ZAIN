from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    email = models.CharField(
        verbose_name = 'Email.com',
        max_length = 255
    )
    phone = models.CharField(
        verbose_name= "phone",
        max_length=255
    )
    subject = models.CharField(
        verbose_name = 'Предмет',
        max_length = 255
    )
    message = models.CharField(
        verbose_name = 'Сообшение: ',
        max_length = 255
    )

    def _str__(self):
        return f'{self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'