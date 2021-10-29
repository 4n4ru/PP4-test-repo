from django.contrib import admin
from .models import Meal


# Register your models here.
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['meal_name', 'meal_plan', 'day', 'meal_type']
    list_filter = ['meal_name', 'meal_plan', 'day', 'meal_type']
    search_fields = ['meal_name', 'meal_plan', 'day', 'meal_type']
