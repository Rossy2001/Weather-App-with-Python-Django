# Generated by Django 4.0.1 on 2022-07-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0004_remove_contact_subject_contact_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(default='', max_length=15),
        ),
    ]