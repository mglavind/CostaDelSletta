# Generated by Django 4.2.6 on 2023-10-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bruger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
