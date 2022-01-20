from .models import *
from django.forms import ModelForm, NumberInput, Select, DateInput
from django import forms


# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'task']
#         widgets = {
#             'title': TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': "please enter the title"
#             }),
#             'task': Textarea(attrs={
#                 'class': "form-control",
#                 'placeholder': "describe the expense"
#             }),
#         }


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ["amount", "date", "category"]
        choices = CATEGORY_INCOME
        widgets = {"amount": NumberInput(attrs={'class': "form-control", 'placeholder': 'Input amount'}),
                   "date": DateInput(attrs={"class": "form-control", 'placeholder': 'Input date'}),
                   "choices": Select(choices=choices,
                                     attrs={"class": "form-control", 'placeholder': 'Select category'})}


class ExpenceForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["amount", "date", "category"]
        choices = CATEGORY_EXPENCE
        widgets = {"amount": NumberInput(attrs={'class': "form-control", 'placeholder': 'Input amount'}),
                   "date": DateInput(attrs={"class": "form-control", 'placeholder': 'Input date'}),
                   "choices": Select(choices=choices,
                                     attrs={"class": "form-control", 'placeholder': 'Select category'})}


class GetStatsForPeriod(forms.Form):
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2100)))
    end_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2100)))
