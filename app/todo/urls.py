from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=r'/?')
router.register(r'', views.TodoListViewSet, basename='todos')

urlpatterns = [
  path('todo/', include((router.urls, 'todo service'))),
]
