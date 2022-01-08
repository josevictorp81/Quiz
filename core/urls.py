from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.ListCreateCategory.as_view(), name='category'),
    path('quiz/', views.ListCreateQuiz.as_view(), name='quiz'),
    path('quiz/<int:pk>/', views.RetrieveUpdateDestroyQuiz.as_view(), name='update-destroy-quiz'),
    path('quiz/<str:topic>/', views.Question.as_view(), name='question'),
    path('quiz/<str:topic>/random/', views.RandomQuestion.as_view(), name='random'),
]