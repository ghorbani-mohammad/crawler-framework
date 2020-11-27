# Generated by Django 3.0.5 on 2020-09-04 11:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0027_remove_structure_news_meta_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'agencies'},
        ),
        migrations.AlterField(
            model_name='page',
            name='crawl_interval',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='structure',
            name='news_links_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='structure',
            name='news_meta_structure',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]