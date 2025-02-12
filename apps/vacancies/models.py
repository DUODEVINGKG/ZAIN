from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(
        max_length = 255, 
        verbose_name = "Название вакансии"
    )
    
    photo = models.ImageField(
        upload_to="photo",
        verbose_name="Фотография"
    )
    
    description = models.TextField(
        verbose_name = "Описание работы (Требование, обязанности)"
    )
    country = models.CharField(
        verbose_name="Страна",
        max_length=155,
    )
    created = models.DateField(
        auto_now_add = True,
        blank = True,null = True
    )
    salary = models.CharField(
        max_length=100,
        verbose_name="Зарплата"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
    