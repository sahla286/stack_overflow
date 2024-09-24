from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from api.serializer import UserSerializer,QuestionSerializer
from .models import Questions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class QuestionsView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    
    def create(self, request, *args, **kwargs):
        user=request.user
        ser=QuestionSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=user)
            return Response(data=ser.data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        user=request.user
        questions=self.queryset.filter(user=user)
        serializer=self.serializer_class(questions,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

