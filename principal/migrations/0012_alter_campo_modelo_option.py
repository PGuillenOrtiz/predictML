# Generated by Django 3.2 on 2022-08-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_campo_modelo_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo_modelo',
            name='option',
            field=models.JSONField(null=True),
        ),
    ]