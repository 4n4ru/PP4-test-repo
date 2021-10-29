from django.db import models


class Meal(models.Model):
    meal_name = models.CharField(max_length=50)
    meal_plan = models.CharField(max_length=50)
    day = models.DateField()
    meal_type = models.CharField(max_length=20)
