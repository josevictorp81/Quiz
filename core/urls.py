from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.Category.as_view(), name='category'),
    path('category/<str:topic>/quiz/', views.QuizCategory.as_view(), name='quiz-category'),
    path('quiz/', views.Quiz.as_view(), name='quiz'),
    path('quiz/<str:topic>/', views.Question.as_view(), name='question'),
    path('quiz/<str:topic>/random/', views.RandomQuestion.as_view(), name='random'),
]