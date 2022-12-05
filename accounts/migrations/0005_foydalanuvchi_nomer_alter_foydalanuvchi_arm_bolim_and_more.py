# Generated by Django 4.1.1 on 2022-09-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_foydalanuvchi_arm_bolim'),
    ]

    operations = [
        migrations.AddField(
            model_name='foydalanuvchi',
            name='nomer',
            field=models.IntegerField(default=1, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='arm_bolim',
            field=models.CharField(blank=True, choices=[('arm-1', 'arm-1'), ('arm-2', 'arm-2'), ('arm-3', 'arm-3'), ('arm-4', 'arm-4')], max_length=100, verbose_name='ARM bo`lim'),
        ),
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='lavozimi',
            field=models.CharField(blank=True, choices=[('o`qtuvchi', 'o`qtuvchi'), ('talaba', 'talaba')], max_length=200, verbose_name='Lavozim'),
        ),
    ]
