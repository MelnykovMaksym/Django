from django.contrib import admin
from .models import Income
from .models import Expense

admin.site.register(Income)
admin.site.register(Expense)