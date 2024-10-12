from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import validators
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from asgiref.sync import async_to_sync
from pathlib import Path
import json
from . import instagram


output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)

# Serializer to handle incoming URL data
class URLSerializer(serializers.Serializer):
    url = serializers.URLField(
        default='https://www.instagram.com/p/C_9l_-cTFJV/?igsh=N2Mwd3JyOWYzamFl',
    )

class ProcessURLView(APIView):
    @swagger_auto_schema(
        request_body=URLSerializer,
        responses={200: openapi.Response('URL processed', URLSerializer)}
    )
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data.get('url')
            # You can add more logic to process the URL here
            if validators.url(url):
                # Perform your custom logic here
                print("running Instagram scrape and saving results to ./results directory")
                # sync_to_async
                post_multi_image = async_to_sync(instagram.scrape_post_with_httpx)(url)
                output.joinpath("food-multi-image-post-use-httpx-with-parse-post-function.json").write_text(json.dumps(post_multi_image, indent=2, ensure_ascii=False), encoding='utf-8')
                return Response({"message": "URL is valid", "result": post_multi_image}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid URL"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer