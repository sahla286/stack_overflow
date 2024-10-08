from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken 

router=DefaultRouter()

router.register('users',views.UserView,basename='users')
router.register('question',views.QuestionsView,basename='question')
router.register('userquestion',views.UserQuestionsView,basename='userquestion')
router.register('answer',views.AnswerView,basename='answer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token',ObtainAuthToken.as_view()),

] + router.urls
