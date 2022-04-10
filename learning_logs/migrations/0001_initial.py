# Generated by Django 3.2.11 on 2022-01-30 03:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='記事タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('is_public', models.BooleanField(default=True, verbose_name='公開可能ですか？')),
                ('description', models.TextField(max_length=130, verbose_name='記事の説明')),
                ('keywords', models.CharField(default='記事のキーワード', max_length=255, verbose_name='記事のキーワード')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('relation_posts', models.ManyToManyField(blank=True, related_name='_learning_logs_post_relation_posts_+', to='learning_logs.Post', verbose_name='関連記事')),
                ('tags', models.ManyToManyField(blank=True, to='learning_logs.Tag', verbose_name='タグ')),
            ],
        ),
    ]
