from django.urls import path
from .views import KeywordExtractor

urlpatterns = [
    path('keyword-extractor', KeywordExtractor.as_view())
]
