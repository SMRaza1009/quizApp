from django.shortcuts import render
from quizApp.models import BaseModel, Topic, Question, Option, UserResponse
from quizApp.serializers import TopicSerializer, QuestionSerializer, OptionSerializer, UserResponseSerializer
from django.contrib.auth.models import User
from  rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class OptionList(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer    

class OptionDetail(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer 
                   


# Create your views here.
# class TopicViewSet(viewsets.ModelViewSet):
#     queryset = Topic.objects.all()
#     serializer_class = TopicSerializer
    
    
# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class OptionViewSet(viewsets.ModelViewSet):
#     queryset = Option.objects.all()
#     serializer_class = OptionSerializer

# class UserResponseViewSet(viewsets.ModelViewSet):
#     queryset = UserResponse.objects.all()
#     serializer_class = UserResponseSerializer


    