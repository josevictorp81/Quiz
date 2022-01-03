from django.urls import path

from . import views

urlpatterns = [
    path('', views.Quiz.as_view(), name='quiz'),
    path('<str:topic>/', views.Question.as_view(), name='question'),
    path('<str:topic>/random/', views.RandomQuestion.as_view(), name='random'),
]