from django import forms
from .models import Meal


class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ('meal_name', 'meal_plan', 'day', 'meal_type')
