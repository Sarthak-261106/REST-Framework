from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostProcessor
from rest_framework import filters
# Create your views here.

class HelloWorldView(APIView):
    def get(self,request):
        return Response({'message':'hello world'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostProcessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content']


    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
