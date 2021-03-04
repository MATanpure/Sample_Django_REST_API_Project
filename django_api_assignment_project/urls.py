from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiapp.urls')),
    # path('api-token-auth/', obtain_jwt_token),
    # path('refresh-jwt-token/', refresh_jwt_token),
    # path('verify-jwt-token/', verify_jwt_token),
]
