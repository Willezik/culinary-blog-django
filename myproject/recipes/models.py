from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('dessert', 'Десерт'),
        ('drink', 'Напиток'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.IntegerField(verbose_name='Время приготовления (мин)')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Категория')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True, verbose_name='Фото блюда')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'