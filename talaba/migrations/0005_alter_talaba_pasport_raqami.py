# Generated by Django 4.1.1 on 2022-09-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talaba', '0004_alter_talaba_pasport_raqami_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talaba',
            name='pasport_raqami',
            field=models.IntegerField(),
        ),
    ]
