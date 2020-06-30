from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.TextField()
    post_image = serializers.ImageField()
    author_id = serializers.IntegerField()