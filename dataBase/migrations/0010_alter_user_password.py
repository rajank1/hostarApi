# Generated by Django 4.0.1 on 2023-06-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataBase', '0009_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=107),
        ),
    ]
