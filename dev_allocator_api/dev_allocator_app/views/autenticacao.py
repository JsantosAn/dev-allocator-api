from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView




class CustomTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(operation_description="Verify the token")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(operation_description="Obtain a new token pair")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(operation_description="Refresh the token")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)