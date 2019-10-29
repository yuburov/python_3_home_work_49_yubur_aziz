from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserChangeView, UserChangePassword

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<pk>/edit/', UserChangeView.as_view(), name='user_update'),
    path('profile/<pk>/change-password/', UserChangePassword.as_view(), name='user_change_password')
]

app_name = 'accounts'