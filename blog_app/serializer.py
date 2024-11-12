from rest_framework import serializers
from blog_app.models import Blog

class BlogSerializsers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()


    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    