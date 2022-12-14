# Generated by Django 4.1.1 on 2022-10-01 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formulyar_raqami', models.CharField(max_length=200)),
                ('tel_raqami', models.CharField(max_length=200)),
                ('pasport_seryasi', models.CharField(max_length=200)),
                ('pasport_raqami', models.CharField(max_length=200)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('foy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
