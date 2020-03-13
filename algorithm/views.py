from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import yake


class KeywordExtractor(APIView):
    def post(self, request):
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(request.data.get('text'))
        keywords.sort(key=lambda x: x[1])
        return Response([keyword[0] for keyword in keywords])
