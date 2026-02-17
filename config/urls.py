from django.contrib import admin
from django.urls import path, include
from .views import login_view, dashboard_view, chat_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', login_view),
    path('dashboard/', dashboard_view),
    path('chat/<int:room_id>/', chat_view),

    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]