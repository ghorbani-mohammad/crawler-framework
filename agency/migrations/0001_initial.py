# Generated by Django 3.0.5 on 2021-02-25 15:44
# Generated by Django 3.0.5 on 2020-12-18 10:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('country', models.CharField(default='NA', max_length=20)),
                ('website', models.CharField(max_length=100, unique=True)),
                ('alexa_global_rank', models.IntegerField(default=0, null=True)),
                ('crawl_headers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('status', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'agencies',
            },
        ),
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('key_values', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000, unique=True)),
                ('crawl_interval', models.PositiveIntegerField(default=60, help_text='minute')),
                ('load_sleep', models.PositiveIntegerField(blank=True, default=4, help_text='each link sleep')),
                ('links_sleep', models.PositiveIntegerField(blank=True, default=1, help_text='all links sleep')),
                ('last_crawl', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=1)),
                ('fetch_content', models.BooleanField(default=1)),
                ('telegram_channel', models.CharField(blank=True, help_text='like: @jobinja', max_length=100, null=True)),
                ('iv_code', models.CharField(blank=True, max_length=100, null=True)),
                ('message_code', models.TextField(blank=True, default=None, help_text='message=data["link"] or data["iv_link"]', null=True)),
                ('take_picture', models.BooleanField(default=False)),
                ('lock', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='agency.Agency')),
                ('cookie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='agency.Cookie')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('news_links_structure', django.contrib.postgres.fields.jsonb.JSONField()),
                ('news_links_code', models.TextField(blank=True, help_text='like: for el in elements: try: links.append(el["href"]) except: continue', null=True)),
                ('news_meta_structure', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=300, null=True)),
                ('fetched_links', models.IntegerField(default=0)),
                ('new_links', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='.static/crawler/static')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='agency.Page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agency.Structure'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField(default='')),
                ('error', models.TextField(null=True)),
                ('phase', models.CharField(blank=True, choices=[('cra', 'کرال'), ('sen', 'ارسال به تلگرام')], max_length=3, null=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='agency.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
