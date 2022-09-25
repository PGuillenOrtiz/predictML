# Generated by Django 3.2 on 2022-09-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_personaldata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principal',
            old_name='description',
            new_name='partial_description',
        ),
        migrations.AddField(
            model_name='principal',
            name='full_description',
            field=models.TextField(max_length=600, null=True),
        ),
    ]