# Generated by Django 4.2.6 on 2023-10-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poster', '0002_hold_alter_godkendelse_hold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='godkendelse',
            name='status',
            field=models.CharField(choices=[('Afventer', 'Afventer'), ('Godkendt', 'Godkendt'), ('Rejected', 'Rejected')], default='Afventer', max_length=10),
        ),
    ]