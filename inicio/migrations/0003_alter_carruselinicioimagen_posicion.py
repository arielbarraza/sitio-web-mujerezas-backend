# Generated by Django 5.0.6 on 2024-10-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_carruselinicioimagen_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carruselinicioimagen',
            name='posicion',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
