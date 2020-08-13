from rest_framework import routers
from .views import Todoclass,Hi
from django.urls import path,include

router= routers.DefaultRouter()
router.register('todo',Todoclass,'todo')


urlpatterns=[
    path('api',include(router.urls)),
    path('hi',Hi),
]