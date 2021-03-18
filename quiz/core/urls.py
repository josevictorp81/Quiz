from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.Quiz.as_view(), name='quiz'),
]