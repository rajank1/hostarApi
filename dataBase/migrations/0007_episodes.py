# Generated by Django 4.0.1 on 2023-06-19 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataBase', '0006_starbharat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_no', models.IntegerField(default=-1)),
                ('decribtion', models.CharField(default='', max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataBase.shows')),
            ],
        ),
    ]