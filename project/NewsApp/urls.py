from django.urls import path
from .views import *

urlpatterns = [
    path('news/', Post_List.as_view(), name='fb'),
    path('post/<int:pk>/', Posts.as_view(), name='Post_list'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('articles/create/', PostCreateArticles.as_view(), name='post_create_articles'),
    path('news/<int:pk>/edit/', Postedit.as_view(), name='post_update'),
# Придумать как исправить удаление, чтобы выводилась инфа о том что удаляется.
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>/edit/', PosteditArticles.as_view(), name='post_update'),
#Придумать как исправить удаление, чтобы выводилась инфа о том что удаляется.
    path('articles/<int:pk>/delete/', PostDeleteArticles.as_view(), name='post_delete'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
]