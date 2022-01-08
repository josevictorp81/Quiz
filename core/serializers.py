from rest_framework import serializers

from .models import Question, Quizzes, Answer, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Quizzes
        fields = ['id', 'title', 'category']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer_text', 'is_right']


class ListAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'title']


class ListQuestionSerializer(serializers.ModelSerializer):
    answer = ListAnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'title', 'answer']


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = ListAnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['title', 'answer']
