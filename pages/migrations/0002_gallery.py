# Generated by Django 3.1.7 on 2021-03-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
        ),
    ]
