# Generated by Django 5.0.6 on 2024-10-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsulas', '0003_remove_capsula_url_capsula_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsula',
            name='archivo',
            field=models.FileField(upload_to='archivos/capsulas'),
        ),
    ]
