# Generated by Django 3.2 on 2022-09-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_campo_modelo_notebook_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo_modelo',
            name='notebook_model',
        ),
        migrations.AddField(
            model_name='principal',
            name='notebook_model',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
