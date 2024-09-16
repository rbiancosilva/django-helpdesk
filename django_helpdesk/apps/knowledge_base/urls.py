from django.urls import path

from . import views
from .views import  AllArticleListView, ArticleListView, ArticleDetailView, new_article_knowledge_base 

urlpatterns = [

    path('', AllArticleListView.as_view(), name='index_knowledge_base'), #SIDE BAR (FILTER)
    path('details/<int:pk>', ArticleDetailView.as_view(), name='details_knowledge_base'),
    path('my_articles', ArticleListView.as_view(), name='my_articles_knowledge_base'),
    path('new', views.new_article_knowledge_base, name='new_knowledge_base'),
 
]