from rest_framework import serializers
from .models import *


# logo
class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'


# slider
class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


# about
class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


# direction
class DirectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


# task
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# resitrations
class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


# result
class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


# contact
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# questions
class QuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


# answer
class AnswersSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Answers
        fields = '__all__'


# letter
class LetterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'