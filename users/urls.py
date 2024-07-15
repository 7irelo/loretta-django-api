from django.urls import path
from .views import CreateUserView, UserDetailView, RegisterUserView, LoginUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
]
