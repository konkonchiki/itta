from logging import Logger
from turtle import title
from django.shortcuts import render , redirect
from django.template import context
from .models import Post , Tag


# トップページ
def index(request):
    titles      = Post.objects.order_by('-create_at')
    context     = { 'titles' : titles }
    return render(request,'learning_logs/index.html',context)

def article(request,title_id):
    post        = Post.objects.get(id=title_id)
    context     = {'post':post}
    return render(request,'learning_logs/article.html',context)

def tag(request,tag_id):
    titles          = Post.objects.all()
    tag             = Tag.objects.get(id=tag_id)
    title_search    = filter(lambda titles : tag in titles.tags.all(),titles)
    context         = {'titles':title_search}
    return render(request,'learning_logs/tags.html',context)