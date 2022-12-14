# Generated by Django 4.1.1 on 2022-10-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ism', '0002_ism_delete_surname'),
        ('sharif', '0002_sharif_author'),
        ('familiya', '0001_initial'),
        ('arm_2', '0005_arm_2_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba_kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invertor', models.CharField(max_length=200)),
                ('kitob', models.CharField(max_length=200, verbose_name='Kitob nomi')),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('familya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familiya.familiya')),
                ('ism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ism.ism')),
                ('sharifi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharif.sharif')),
            ],
        ),
    ]
