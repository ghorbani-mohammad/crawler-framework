# Generated by Django 3.0.5 on 2020-08-30 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0024_auto_20200830_0842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CrawlReport',
            new_name='Report',
        ),
    ]