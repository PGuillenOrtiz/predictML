# Generated by Django 3.2 on 2022-09-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_auto_20220910_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='full_description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]