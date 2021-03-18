from rest_framework import serializers

from .models import Question, Quizzes, Answer, Category

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title',]