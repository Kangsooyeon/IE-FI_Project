from rest_framework import serializers
from .models import *


class ArticleListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'nickname', 'created_at')

    def get_nickname(self, obj):
        return obj.user.nickname


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article')

    def get_nickname(self, obj):
        return obj.user.nickname
    

class ArticleSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

    def get_nickname(self, obj):
        return obj.user.nickname

