from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class Category_of_coursesView(ListAPIView):
    queryset = Course_Category.objects.all()
    serializer_class = Category_of_coursesSerializerlist

class MentorsView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class VacansyView(ListAPIView):
    queryset = Vacansy.objects.all()
    serializer_class = VacanseSerializers

class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
class EmailViews(ListAPIView):
    queryset = News_email.objects.all()
    serializer_class = EmailSerializers
@api_view(['GET'])
def Category_of_courseView(request,category_id):
    category = get_object_or_404(Course_Category,id=category_id)
    serializers = Category_of_coursesSeriaizerdetial(category,context={'request':request})
    return Response(serializers.data)

@api_view(['POST'])
def EmailView(request):
    news_id = request.data.get('news_id')
    email = request.data.get('email')
    if not email:
        return Response({'error': 'email обязателен'}, status=status.HTTP_400_BAD_REQUEST)
    if not news_id:
        return Response({'error': 'news_id обязателен'}, status=status.HTTP_400_BAD_REQUEST)
    news = get_object_or_404(News, id=news_id)
    serializer = EmailSerializers(data={'email': email})
    if serializer.is_valid():
        email_obj, created = News_email.objects.get_or_create(email=email)
        news.new_email.add(email_obj)
        news.ordered_places = (news.ordered_places or 0) + 1
        news.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
