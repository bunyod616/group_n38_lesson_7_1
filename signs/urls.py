from django.urls import path
from .views import ListCategoryAPIView, ListRoadSignsAPIView

urlpatterns = [
    path('category-list', ListCategoryAPIView.as_view(), name='category-list'),
    path('road-signs-list', ListRoadSignsAPIView.as_view(), name='road-signs-list'),
]