# Generated by Django 5.0.2 on 2024-03-01 01:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=255, unique_for_date='published_at')),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published_at',),
                'indexes': [models.Index(fields=['slug', 'published_at'], name='blog_post_slug_64cf80_idx')],
            },
        ),
    ]
