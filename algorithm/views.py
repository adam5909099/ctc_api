from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import yake


class KeywordExtractor(APIView):
    def post(self, request):
        kw_extractor = yake.KeywordExtractor(top=50)
        keywords = kw_extractor.extract_keywords(request.data.get('text'))
        return Response([keyword[0] for keyword in keywords])
