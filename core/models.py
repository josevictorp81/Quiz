from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    title = models.CharField(max_length=255, default='New Quiz', verbose_name='Quiz Title')
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']

    def __str__(self):
        return self.title


class Question(models.Model):
    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name='Type of Question')
    title = models.CharField(max_length=255, verbose_name='Title')
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name='Difficulty')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    updated = models.DateTimeField(verbose_name='Last Updated', auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='Active Status')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)
    updated = models.DateTimeField(verbose_name='Last Updated', auto_now=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['id']

    def __str__(self):
        return self.answer_text