from rest_framework import generics

from .models import Question, Quizzes, Answer, Category
from .serializers import QuizSerializer

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer
