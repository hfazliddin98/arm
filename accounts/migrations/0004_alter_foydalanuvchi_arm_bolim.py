# Generated by Django 4.1.1 on 2022-09-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_foydalanuvchi_arm_bolim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='arm_bolim',
            field=models.CharField(blank=True, choices=[('arm-1', 'arm-1'), ('arm-2', 'arm-2'), ('arm-3', 'arm-3'), ('arm-4', 'arm-4'), ('talaba', 'talaba')], max_length=100, verbose_name='ARM bo`lim'),
        ),
    ]
