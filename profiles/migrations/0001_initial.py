# Generated by Django 4.0.4 on 2022-06-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
