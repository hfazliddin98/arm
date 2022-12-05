# Generated by Django 4.1.1 on 2022-09-25 13:45

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('talaba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talaba',
            name='tel_raqami',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]