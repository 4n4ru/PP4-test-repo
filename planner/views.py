from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Meal
from .forms import MealForm


def meal_view(request):
    if request.method == 'POST':
        meals = formset_factory(MealForm, extra=21)
        formset = meals(request.POST)
        if formset.is_valid():
            for form in formset:
                meal_name = form.cleaned_data.get('meal_name')
                meal_type = form.cleaned_data.get('meal_type')
                meal_day = form.cleaned_data.get('day')
                meal_plan = form.cleaned_data.get('meal_plan')
                if meal_name:
                    Meal(
                        meal_name=meal_name,
                        meal_plan=meal_plan,
                        day=meal_day,
                        meal_type=meal_type
                    ).save()
            return redirect(meal_view)
    else:
        meals = formset_factory(MealForm, extra=3)
        formset = meals()
        return render(request, 'meal.html', {'formset': formset})
