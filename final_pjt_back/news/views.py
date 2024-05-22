from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.request
import json

from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# 추후 네이버 뉴스 API 키 숨김 필요
client_id = "oZp0myvPwtjsxvZxfemw"
client_secret = "0dJKbcrtfz"
# Create your views here.

@api_view(['GET'])
def search_finance(django_request):
    encText = urllib.parse.quote("금융")
    url = "https://openapi.naver.com/v1/search/news?query="+encText+"&display=10"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')  
    response_json = json.loads(response_body)
    for item in response_json['items']:
        item['title'] = item['title'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')
        item['description'] = item['description'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')

        # okt = Okt()
        # description = ' '.join(word for word, pos in okt.pos(item['description']) if pos in ['Noun'])

        # remove_words = ["금융", "기자"]
        # description = ' '.join(word for word in description.split() if word not in remove_words)

        # print(description)
        # vectorizer = TfidfVectorizer()
        # tfidf_matrix = vectorizer.fit_transform([description])
        # scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf_matrix.sum(axis=0)).ravel())
        # sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # keyword = sorted_scores[0]
        # item['keyword'] = keyword

    return Response(response_json)

@api_view(['GET'])
def search_economy(request):
    encText = urllib.parse.quote("경제")
    url = "https://openapi.naver.com/v1/search/news?query="+encText+"&display=10"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')  
    response_json = json.loads(response_body)
    for item in response_json['items']:
        item['title'] = item['title'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')
        item['description'] = item['description'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')

        # okt = Okt()
        # description = ' '.join(word for word, pos in okt.pos(item['description']) if pos in ['Noun'])

        # remove_words = ["경제", "기자"]
        # description = ' '.join(word for word in description.split() if word not in remove_words)

        # vectorizer = TfidfVectorizer()
        # tfidf_matrix = vectorizer.fit_transform([description])
        # scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf_matrix.sum(axis=0)).ravel())
        # sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # keyword = sorted_scores[0]
        # item['keyword'] = keyword
    return Response(response_json)

@api_view(['GET'])
def search_stock(request):
    encText = urllib.parse.quote("주식")
    url = "https://openapi.naver.com/v1/search/news?query="+encText+"&display=10"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')  
    response_json = json.loads(response_body)
    for item in response_json['items']:
        item['title'] = item['title'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')
        item['description'] = item['description'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')

        # okt = Okt()
        # description = ' '.join(word for word, pos in okt.pos(item['description']) if pos in ['Noun'])

        # remove_words = ["주식", "기자"]
        # description = ' '.join(word for word in description.split() if word not in remove_words)

        # vectorizer = TfidfVectorizer()
        # tfidf_matrix = vectorizer.fit_transform([description])
        # scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf_matrix.sum(axis=0)).ravel())
        # sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # keyword = sorted_scores[0]
        # item['keyword'] = keyword
    return Response(response_json)

@api_view(['GET'])
def search_coin(request):
    encText = urllib.parse.quote("코인")
    url = "https://openapi.naver.com/v1/search/news?query="+encText+"&display=10"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')  
    response_json = json.loads(response_body)
    for item in response_json['items']:
        item['title'] = item['title'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')
        item['description'] = item['description'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')

        # okt = Okt()
        # description = ' '.join(word for word, pos in okt.pos(item['description']) if pos in ['Noun'])

        # remove_words = ["코인", "기자"]
        # description = ' '.join(word for word in description.split() if word not in remove_words)

        # vectorizer = TfidfVectorizer()
        # tfidf_matrix = vectorizer.fit_transform([description])
        # scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf_matrix.sum(axis=0)).ravel())
        # sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # keyword = sorted_scores[0]
        # item['keyword'] = keyword
    return Response(response_json)