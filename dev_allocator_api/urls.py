
from django.contrib import admin
from django.urls import path, include
from dev_allocator_app.swagger import schema_view
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', lambda request: redirect('swagger/')),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include('dev_allocator_app.urls')), ]
