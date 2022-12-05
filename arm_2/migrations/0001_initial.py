# Generated by Django 4.1.1 on 2022-09-28 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guruh', '0001_initial'),
        ('tuman', '0002_tuman_author'),
        ('ism', '0002_ism_delete_surname'),
        ('viloyat', '0002_viloyat_author'),
        ('familiya', '0001_initial'),
        ('yonalish', '0001_initial'),
        ('fakultet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharif', '0002_sharif_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arm_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formulyar_raqami', models.CharField(max_length=200)),
                ('darajasi', models.CharField(choices=[('bakalavr', 'bakalavr'), ('magistr', 'magistr')], max_length=200)),
                ('kurs', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=200)),
                ('tugilgan_kun_oy_yil', models.CharField(max_length=100, verbose_name='Tug`ilgan kun/oy/yil')),
                ('kocha_uy', models.CharField(max_length=200)),
                ('tel_raqami', models.CharField(max_length=200)),
                ('pasport_seryasi', models.CharField(max_length=200)),
                ('pasport_raqami', models.CharField(max_length=200)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fakultet.fakultet')),
                ('familya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familiya.familiya')),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruh.guruh')),
                ('ism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ism.ism')),
                ('sharifi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharif.sharif')),
                ('tuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuman.tuman')),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viloyat.viloyat')),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yonalish.yonalish')),
            ],
        ),
    ]
