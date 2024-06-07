# Generated by Django 4.2 on 2024-06-02 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samurai', '0005_alter_samurai_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='samurai',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='samurais', to='samurai.category'),
        ),
        migrations.AddField(
            model_name='samurai',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='samurai.posttag'),
        ),
    ]