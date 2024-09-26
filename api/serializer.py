from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Questions,Answers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)

class AnswerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class AnswerSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) 
    datetime=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    upvote=AnswerUserSerializer(read_only=True,many=True)
    upvote_count=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields='__all__'


    
class QuestionSerializer(serializers.ModelSerializer):
    qus_ans=AnswerSerializer(read_only=True,many=True)
    user=serializers.CharField(read_only=True) 
    datetime=serializers.CharField(read_only=True)
    
    class Meta:
        model=Questions
        fields='__all__'



    

        

