
from django.urls import path, include
from .views import article_list, article_update, ArticleViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('article', ArticleViewSet, basename= 'testname')

urlpatterns = [
    path('viewset/', include(routers.urls)),
    #path('article/', article_list, name = 'article_list'),
    #path('articleDetail/<int:pk>/', article_update)
]
