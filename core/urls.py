from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.ListCreateCategory.as_view(), name='category'),
    path('quiz/', views.ListCreateQuiz.as_view(), name='quiz'),
    path('quiz/<int:pk>/', views.RetrieveUpdateDestroyQuiz.as_view(), name='update-destroy-quiz'),
    path('question/', views.CreateQuestion.as_view(), name='create-question'),
    path('question/<int:pk>/', views.RetrieveUpdateDestroyQuestion.as_view(), name='update-destroy-question'),
    path('question/<str:quiz>/', views.ListQuestion.as_view(), name='list-question'),
    path('question/<str:quiz>/random/', views.ListRandomQuestion.as_view(), name='list-random-question'),
    path('answer/', views.ListCreateAnswer.as_view(), name='list-create-answer'),
    path('answer/<int:pk>/', views.RetieveUpdateDestroyAnswer.as_view(), name='update-destroy-answer'),
]