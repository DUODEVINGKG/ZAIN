from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Banner(models.Model):
    title = models.CharField(
        max_length= 100,
        verbose_name="Зоголовок"
    )
    photo = models.ImageField(
        upload_to="photo",
        verbose_name="Фотография"
    )
    photo2 = models.ImageField(
        verbose_name="Вторая Фотография",
        upload_to="photo"
    )
    
    
    def save(self, *args, **kwargs):
        if not self.pk and Banner.objects.exists():
            raise ValidationError("Можно добавить только один баннер!")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"
        
        
        
class Counter(models.Model):
    
    partners = models.PositiveIntegerField(
        verbose_name = "Наши партнеры"
    )
    
    сurrent_employees = models.PositiveIntegerField(
        verbose_name = "Текущие работники"
    )
    
    free_vacancies = models.PositiveIntegerField(
        verbose_name = "Свободные вакансии"
    )
    
    happy_clients = models.PositiveIntegerField(
        verbose_name = "Счастливые клиенты"
    )
        
    def __str__(self):
        return "Данные о счетчике"
    
    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчик"
               
        
class Base(models.Model):
    email = models.EmailField(
        max_length=100,
        verbose_name="Электронная почта"
    )
    phone = models.CharField(
        verbose_name="Номер телеофона",
        max_length=155,
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Адресс"
    )
    instagram = models.URLField(
        verbose_name="Инстаграмм",
        null=True, blank=True
    )
    whatsapp = models.URLField(
        verbose_name="Ватсапп",
        null=True, blank=True
    )
    telegram = models.URLField(
        verbose_name="телеграм",
        null=True, blank=True
    )

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    


class Reviews(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя клиента"
    ) 
    
    photo = models.ImageField(
        upload_to="photo",
        verbose_name="Фотография клиента"
    )
    
    description = models.TextField(
        verbose_name = "Отзыв клиента"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    
class File(models.Model):
    file = models.FileField(null=True,blank= True,upload_to='files/', verbose_name= 'Файл')

    

    class Meta:
        verbose_name = 'Документ',
        verbose_name_plural = 'Документы'