# Generated by Django 4.2.6 on 2023-10-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('date_priv', models.DateField(auto_now_add=True, verbose_name='Дата поставки')),
                ('date_snat', models.DateField(verbose_name='До какого числа')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['-date_snat'],
            },
        ),
    ]
