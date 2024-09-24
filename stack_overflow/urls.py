from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('users',views.UserView,basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
