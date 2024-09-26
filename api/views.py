from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from django.contrib.auth.models import User
from api.serializer import UserSerializer,QuestionSerializer,AnswerSerializer
from .models import Questions,Answers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import serializers

# Create your views here.

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class QuestionsView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    
    def create(self,request,*args,**kwargs):
        user=request.user
        ser=QuestionSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=user)
            return Response(data=ser.data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST'],detail=True)
    def add_answer(self,request,*args,**kw):
        id = kw.get('pk')
        user=request.user
        question=Questions.objects.get(id=id)
        ser=AnswerSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=user,question=question)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserQuestionsView(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request,*args,**kwargs):
        user=request.user
        questions=Questions.objects.filter(user=user) 
        ser=QuestionSerializer(questions,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)

class AnswerView(ModelViewSet):
    serializer_class=AnswerSerializer
    queryset=Answers.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def list(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def destroy(self, request, *args, **kw):
        id=kw.get('pk')
        ans=self.queryset.get(id=id)
        if ans.user == request.user :
            ans.delete()
            return Response(data={'msg':'answer deleted'},status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError('not allowed')

    @action(methods=['POST'],detail=True)
    def add_upvote(self,request,*args,**kw):
        id=kw.get('pk')
        ans=self.queryset.get(id=id)
        user=request.user
        ans.upvote.add(user)
        return Response(data={'msg':'vote registerd'},status=status.HTTP_200_OK)



