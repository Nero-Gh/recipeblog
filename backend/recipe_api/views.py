from django.shortcuts import render
from .models import Blog,Category
from .serializers import blogSerializer,categorySerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response


blogview = viewsets.GenericViewSet
bloglist  = mixins.ListModelMixin 
blogretrieve = mixins.RetrieveModelMixin

# Create your views here.

# this class fetches all the data from the blog database
class BlogApi(blogview,bloglist,blogretrieve):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field = 'slug'

# this class fetches all the data from the category database
class CategoryApi(blogview,bloglist,blogretrieve):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    lookup_field = 'id'


# this class fetches all the data from the blog id that matches with the category id.
class CategoryApiPost(viewsets.ViewSet):
    def retrieve(self, request,id=None):
        queryset =Blog.objects.filter(Category=id)
        serializer = categorySerializer(queryset, many=True)
        return Response (serializer.data)