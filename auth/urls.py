from django.urls import path

from .import views

urlpatterns = [
    path('signup/', views.UserCreateAPIView.as_view(), name='signup'),
]
