# Generated by Django 4.1.1 on 2022-09-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0022_alter_principal_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='curriculum',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='principal',
            name='notebook_model',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
