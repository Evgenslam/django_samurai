# Generated by Django 4.2 on 2024-05-17 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samurai', '0003_alter_samurai_is_published_alter_samurai_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='samurai',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='samurai.category'),
        ),
    ]
