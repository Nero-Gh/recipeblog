from ast import pattern
from django.urls import path,include
from .views import BlogApi,CategoryApi,CategoryApiPost
from rest_framework import routers


router = routers.SimpleRouter()
router.register('blogs',BlogApi,basename='blogs')
router.register('category',CategoryApi,basename='category')
router.register('categoryBasedBlog',CategoryApiPost,basename='categoryBasedBlogs')

urlpatterns = [
    path('',include(router.urls))
]




