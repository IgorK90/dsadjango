# Generated by Django 4.1.4 on 2023-02-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('available', models.IntegerField(default=0)),
                ('image', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]
