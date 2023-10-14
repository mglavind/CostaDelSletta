# Generated by Django 4.2.6 on 2023-10-14 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opgave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Godkendelse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('Hold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.bruger')),
                ('Opgave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Poster.opgave')),
            ],
        ),
    ]
