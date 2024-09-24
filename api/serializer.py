from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Questions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
    
class QuestionSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) 
    datetime=serializers.CharField(read_only=True)
    class Meta:
        model=Questions
        fields='__all__'