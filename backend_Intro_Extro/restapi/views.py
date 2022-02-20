from django.shortcuts import render


# viewsets class provides the implementation for CRUD operations by default, what we had to do was specify the serializer class and the query set.

from rest_framework import viewsets          # add this
from .serializers import QuestionAnswerSerializer,AnswerSerializer  # add this
from .models import QuestionAnswer,Answer               # add this


class QuestionAnswerView(viewsets.ModelViewSet):       # add this
    serializer_class = QuestionAnswerSerializer          # add this
    queryset = QuestionAnswer.objects.all()              # add this


class AnswerView(viewsets.ModelViewSet):       # add this
    serializer_class = AnswerSerializer          # add this
    queryset = Answer.objects.all()              # add this
