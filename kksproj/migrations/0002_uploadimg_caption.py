# Generated by Django 4.1 on 2022-08-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kksproj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimg',
            name='caption',
            field=models.CharField(default='UPLOADED IMAGE', max_length=100),
        ),
    ]