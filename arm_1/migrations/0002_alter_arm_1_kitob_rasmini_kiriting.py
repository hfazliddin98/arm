# Generated by Django 4.1.2 on 2022-10-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arm_1',
            name='kitob_rasmini_kiriting',
            field=models.ImageField(null=True, upload_to='rasm/'),
        ),
    ]
