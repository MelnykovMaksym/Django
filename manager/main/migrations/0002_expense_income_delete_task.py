# Generated by Django 4.0.1 on 2022-01-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('food', 'food'), ('appartment rent', 'appartment rent'), ('clothes', 'clothes'), ('other', 'other'), ('education', 'education')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('main work', 'main work'), ('business', 'business'), ('odd job', 'odd job')], max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
