from rest_framework import serializers

from .models import Question, Quizzes, Answer, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate(self, attrs):
        category = Category.objects.filter(name=attrs['name']).first()
        if category:
            raise serializers.ValidationError(detail='Category with this name already existes!')
        return super().validate(attrs)

class QuizSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Quizzes
        fields = ['id', 'title', 'category']
    
    def validate(self, attrs):
        quiz = Quizzes.objects.filter(title=attrs['title']).first()
        if quiz:
            raise serializers.ValidationError(detail='Quiz with this title already existes!')
        return super().validate(attrs)


class ListQuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Quizzes
        fields = ['id', 'title', 'category']
        ready_only_fields = fields


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer_text', 'is_right']
    
    def validate(self, attrs):
        answer = Answer.objects.filter(answer_text=attrs['answer_text']).first()
        if answer:
            raise serializers.ValidationError(detail='Answer already existes!')
        return super().validate(attrs)


class ListAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'title']
    
    def validate(self, attrs):
        question = Question.objects.filter(title=attrs['title']).first()
        if question:
            raise serializers.ValidationError(detail='Quiz with this title already existes!')
        return super().validate(attrs)


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
