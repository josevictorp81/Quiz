from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.ListCreateCategory.as_view(), name='category'),
    path('quiz/', views.ListCreateQuiz.as_view(), name='quiz'),
    path('quiz/<int:pk>/', views.RetrieveUpdateDestroyQuiz.as_view(), name='update-destroy-quiz'),
    path('quiz/question/', views.CreateQuestion.as_view(), name='create-question'),
    path('quiz/question/<int:pk>/', views.RetrieveUpdateDestroyQuestion.as_view(), name='update-destroy-question'),
    path('quiz/<str:topic>/question/', views.ListQuestion.as_view(), name='list-question'),
    path('quiz/<str:topic>/question/random/', views.ListRandomQuestion.as_view(), name='list-random-question'),
]