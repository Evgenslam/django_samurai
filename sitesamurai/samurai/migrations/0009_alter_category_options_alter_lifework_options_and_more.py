# Generated by Django 5.0.6 on 2024-06-09 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samurai', '0008_alter_samurai_lifework'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='lifework',
            options={'verbose_name': 'Дело жизни', 'verbose_name_plural': 'Дела'},
        ),
        migrations.AlterModelOptions(
            name='posttag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterModelOptions(
            name='samurai',
            options={'ordering': ['-time_create'], 'verbose_name': 'Самурай', 'verbose_name_plural': 'Самураи'},
        ),
        migrations.AlterField(
            model_name='samurai',
            name='lifework',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='samurai.lifework'),
        ),
    ]