# Generated by Django 4.1.2 on 2022-10-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_foydalanuvchi_nomer_alter_foydalanuvchi_arm_bolim_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foydalanuvchi',
            name='nomer',
        ),
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='rasm',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]