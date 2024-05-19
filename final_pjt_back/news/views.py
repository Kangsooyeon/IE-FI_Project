from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.request
import json

# Create your views here.
@api_view(['GET'])
def index(request):
    # 추후 네이버 뉴스 API 키 숨김 필요
    client_id = "oZp0myvPwtjsxvZxfemw"
    client_secret = "0dJKbcrtfz"
    
    encText = urllib.parse.quote("은행상품")
    url = "https://openapi.naver.com/v1/search/news?query="+encText+"&display=100"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    response_body = response.read().decode('utf-8')  
    response_json = json.loads(response_body)
    for item in response_json['items']:
        item['title'] = item['title'].replace('&quot;', '').replace('<b>', '').replace('</b>', '')
    return Response(response_json)