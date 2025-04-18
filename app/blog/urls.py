from django.urls import path, include
from .views import Index, Article, DetailArticleView, LikeArticle

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article')
]