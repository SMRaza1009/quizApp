from rest_framework import serializers
from .models import BaseModel, Topic, Question, Option, UserResponse
from django.contrib.auth.models import User


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option 
        fields = "__all__"
        


class QuestionSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = "__all__"
        

# Topic -> (Topic should be in the database) -> Topic
# Question -> (topic, option)
# Options -> 

# Topic
# Options
# Question

    # def create(self, validated_data):
    #     correct_option_id = validated_data.pop('correct_option_id', None)
    #     options_data = validated_data.pop('options', [])

    #     # Create the question without specifying 'correct_option'
    #     question = Question.objects.create(**validated_data)

    #     if correct_option_id:
    #         # Set the 'correct_option' if 'correct_option_id' is provided
    #         correct_option = Option.objects.get(pk=correct_option_id)
    #         question.correct_option = correct_option
    #         question.save()

    #     for option_data in options_data:
    #         Option.objects.create(questions=question, **option_data)

    #     return question


                       