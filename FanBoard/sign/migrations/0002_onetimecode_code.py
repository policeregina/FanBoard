# Generated by Django 4.2 on 2023-04-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimecode',
            name='code',
            field=models.IntegerField(default=None),
        ),
    ]