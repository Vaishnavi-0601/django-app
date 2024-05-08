# Generated by Django 5.0.4 on 2024-05-08 07:36

import djangoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_carlist_chassisnumber_carlist_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroomlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='carlist',
            name='chassisnumber',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[djangoapp.models.alphanumberic]),
        ),
    ]