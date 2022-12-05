# Generated by Django 4.1.1 on 2022-09-25 06:41

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
            name='Dekanat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan', models.CharField(max_length=200)),
                ('adabiyot', models.CharField(max_length=200)),
                ('mualif', models.CharField(max_length=200)),
                ('qollanma', models.CharField(max_length=200)),
                ('nashriyot', models.CharField(max_length=200)),
                ('yili', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]