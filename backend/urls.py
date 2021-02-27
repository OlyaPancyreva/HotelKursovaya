from django.urls import path

from backend.views import *

app_name = 'Backend'
urlpatterns = [
    path('test/create/', TestCreateView.as_view()),
    path('test/all/', TestListView.as_view()),
    path('answer/all/', AnswerListView.as_view()),
    path('answer/create/', AnswerCreateView.as_view()),
    path('profession/all/', ProfessionListView.as_view()),
    path('answer/<int:pk>/', AnswerDetailView.as_view()),
    path('mail/', SendEmailView.as_view()),
]
