# Generated by Django 4.1.2 on 2022-10-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_arm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armadmin',
            name='lavozimi',
            field=models.CharField(choices=[('hodim', 'hodim')], max_length=200, verbose_name='Lavozim'),
        ),
    ]
