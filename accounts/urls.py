from django.urls import path
from .views import RegisterView, ProfileView,AllUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', AllUsersView.as_view(), name='all-users'),
]
