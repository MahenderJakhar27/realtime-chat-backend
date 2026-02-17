from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Register
    path('api/', include('accounts.urls')),

    # Login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/chat/', include('chat.urls')),

]
