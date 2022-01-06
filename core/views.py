from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Quizzes, Answer, Category
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer, CategorySerializer

class Category(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = RandomQuestionSerializer

    def get(self, request, format=None, *args, **kwargs):
        queryset = self.queryset.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

class Question(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, format=None, *args, **kwargs):
        queryset = self.queryset.filter(quiz__title=kwargs['topic'])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
