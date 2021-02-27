from rest_framework import serializers

from backend.models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Test
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmail
        fields = ('mail', 'message')
