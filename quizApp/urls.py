from quizApp.views import QuestionList, QuestionDetail
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

urlpatterns = [
    # Define your API endpoints here
    path('api/questions/', views.QuestionList.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('api/options/', views.OptionList.as_view(), name='option-list'),
    path('api/options/<int:pk>', views.OptionDetail.as_view(), name='option-detail'),
]