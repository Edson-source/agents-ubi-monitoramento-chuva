# Generated by Django 4.2 on 2023-04-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeloUmidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.FloatField()),
                ('data', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
