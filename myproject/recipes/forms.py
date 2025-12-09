from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'cooking_steps', 
                  'cooking_time', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 
                                                 'placeholder': 'Каждый ингредиент с новой строки'}),
            'cooking_steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 8,
                                                   'placeholder': 'Каждый шаг с новой строки'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'cooking_steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (минут)',
            'category': 'Категория',
            'image': 'Фото блюда',
        }
        help_texts = {
            'ingredients': 'Укажите количество и название каждого ингредиента',
            'cooking_steps': 'Опишите процесс приготовления по шагам',
        }