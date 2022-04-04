from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='users-profile'),
    path('register/', views.registerUser, name='users-register'),
    path('', views.getUsers, name='users'),
]