from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, ProjectViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name = 'api_token_auth')
]