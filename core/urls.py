from django.urls import path

from . import views

urlpatterns = [
    path('', views.Quiz.as_view(), name='quiz'),
]