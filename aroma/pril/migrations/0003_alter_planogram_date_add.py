# Generated by Django 4.2.6 on 2023-11-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pril', '0002_planogram_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planogram',
            name='date_add',
            field=models.DateField(verbose_name='дата добавления'),
        ),
    ]
