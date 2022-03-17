from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Question, Quizzes, Answer, Category
from .serializers import QuizSerializer, RandomQuestionSerializer, ListQuestionSerializer, CategorySerializer, QuestionSerializer, AnswerSerializer

class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ListCreateQuiz(generics.ListCreateAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name', 'title']
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyQuiz(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


class CreateQuestion(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class ListQuestion(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        queryset = self.queryset.filter(quiz__title=kwargs['topic'])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class RetrieveUpdateDestroyQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class ListRandomQuestion(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = RandomQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        queryset = self.queryset.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ListCreateAnswer(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class RetieveUpdateDestroyAnswer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
