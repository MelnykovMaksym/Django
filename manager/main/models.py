from django.db import models

CATEGORY_INCOME = (('main work', 'main work'), ('business', 'business'), ('odd job', 'odd job'))
CATEGORY_EXPENCE = (
    ('food', 'food'), ('appartment rent', 'appartment rent'), ('clothes', 'clothes'), ('other', 'other'),
    ('education', 'education'))


class Income(models.Model):
    # this is set of tupples for income category choice. first in tupple represent record in db, second - how user
    # will see it on site.
    Category = CATEGORY_INCOME
    amount = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length=40, choices=Category)

    def __str__(self) -> str:
        return f"{self.category}, {self.amount}, {self.date}"


class Expense(models.Model):
    CATEGORY = CATEGORY_EXPENCE
    amount = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length=40, choices=CATEGORY)

    def __str__(self) -> str:
        return f"{self.category}, {self.amount}, {self.date}"


# class task(models.model):
#     title = models.charfield("sort of costs", max_length=50)
#     task = models.textfield('description')
#
#     def __str__(self):
#         return self.title
#
#     class meta:
#         verbose_name = 'cost accounting'
#         verbose_name_plural = 'costs'
