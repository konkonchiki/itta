from datetime import datetime
from operator import truediv
from time import time
from turtle import title
from venv import create
from django.db import models
from pytz import timezone
from django.utils import timezone

# タグ（１つの記事に複数のタグ）
class Tag(models.Model):
    name = models.CharField('タグ名',max_length=16,unique=True)
    def __str__(self) :
        return self.name

class Post(models.Model):
    """記事"""
    title       = models.CharField('記事タイトル',max_length=32)
    text        = models.TextField('本文')
    tags        = models.ManyToManyField(Tag,verbose_name='タグ',blank=True)
    
    relation_posts = models.ManyToManyField('self',verbose_name='関連記事',blank=True)
    is_public      = models.BooleanField('公開可能ですか？',default=True)
    description    = models.TextField('記事の説明',max_length=130)
    keywords       = models.CharField('記事のキーワード',max_length=255,default='記事のキーワード')
    create_at      = models.DateTimeField('作成日',default=timezone.now)
    updated_at     = models.DateTimeField('更新日',default=timezone.now)
    
    def __str__(self):
        return self.title

