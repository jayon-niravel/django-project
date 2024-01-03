
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Import the Zenpy Class
from zenpy import Zenpy
import logging

# Create your views here.
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer =  ArticleSerializer(articles, many=True)
        # Zenpy accepts an API token
        creds = {
            'email' : 'jniravel@truu.ai',
            'token' : 'F67aiJQK17TEgVxEr8t0eSQPrbgAF5sbwhDObmc9',
            'subdomain': 'truu1662144512'
        }
        zenpy_client = Zenpy(**creds)
        return Response("zenpy_client")

    def create(self, request):
        serializer = ArticleSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, staus = status.HTTP_404_NOT_FOUND)
       

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(article)
        return Response(article)


@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET' :       
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, staus = status.HTTP_404_NOT_FOUND)
       

@csrf_exempt
def article_update(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, status=201)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save();
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    if request.method == 'DELETE':
        article.delete();
        return HttpResponse(status=204)
