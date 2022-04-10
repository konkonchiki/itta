# learning_logs(このアプリ)のURLを操作する

from unicodedata import name
from django.urls import URLPattern, path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #トップページ
    path('',views.index,name='index'),
    path('article/<int:title_id>',views.article,name='article'),
    path('tag/<int:tag_id>',views.tag,name='tag'),
]