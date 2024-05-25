from django.shortcuts import render
from .serializers import CategorySignsSerializer, RoadSignsSerializer
from .models import CategorySigns, RoadSigns
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

    
class ListCategoryAPIView(APIView):
    def get(self, request):
        category = CategorySigns.objects.all()
        serializer = CategorySignsSerializer(category, many=True)
        serializer_data = {
            "category": serializer.data,
            "status": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(serializer.data)
    
class ListRoadSignsAPIView(APIView):
    def get(self, request):
        model = RoadSigns.objects.all()
        serializer = RoadSignsSerializer(model, many=True)
        serializer_data = {
            "model": serializer.data,
            "status": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(serializer_data)
    
class ListRoadSignsAPIView(APIView):
    def get(self, request):
        model = RoadSigns.objects.all()
        serializer = RoadSignsSerializer(model, many=True)
        serializer_data = {
            "model": serializer.data,
            "status": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(serializer_data)