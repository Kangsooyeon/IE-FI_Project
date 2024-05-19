from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import *
from .models import *

# 게시글 List (권한 필요 없음)
@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


# 게시글 생성 (권한 필요)
@api_view(['POST']) 
@permission_classes([IsAuthenticated])    
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 상세 게시글 (권한 필요 없음)
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    print(serializer.data)
    return Response(serializer.data)
    

# 게시글 수정 (권한 필요)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.user:
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# 게시글 삭제 (권한 필요)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.user:
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    article.delete()
    return Response({'message': '게시글 삭제 성공'}, status=status.HTTP_204_NO_CONTENT)

# 댓글 생성 (권한 필요)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=get_object_or_404(Article, pk=article_pk))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 댓글 List (권한 필요 없음)
@api_view(['GET'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 수정 (권한 필요)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comment_update(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 댓글 삭제 (권한 필요)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
    comment.delete()
    return Response({'message': '댓글 삭제 성공'}, status=status.HTTP_204_NO_CONTENT)