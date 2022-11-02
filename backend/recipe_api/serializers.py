from dataclasses import field
from rest_framework import serializers
from .models import Category,Blog


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"