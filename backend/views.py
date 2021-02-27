from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.serializers import *


# GET all
class TestListView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class ProfessionListView(generics.ListAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


# CREATE test
class TestCreateView(generics.CreateAPIView):
    serializer_class = TestSerializer


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerCreateSerializer


# GET, UPDATE, DELETE
class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class SendEmailView(APIView):
    def post(self, request):
        mail = EmailSerializer(data=request.data)
        from_email = request.data.get("mail")
        message = request.data.get("message")
        if mail.is_valid():
            send_mail(subject='Результаты тестирования',
                      message=message,
                      from_email='de.task@mail.ru',
                      recipient_list=[from_email],)
            mail.save()
            return Response(status=201)
        else:
            return Response(status=400)
