# Generated by Django 5.0.6 on 2024-10-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_email_usuario_correo_electronico'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('PUBLICADOR', 'Publicador')], max_length=20),
            preserve_default=False,
        ),
    ]
