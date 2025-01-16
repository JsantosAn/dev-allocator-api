from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from ..models import Developer
from ..serializers import DeveloperSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    @swagger_auto_schema(
        operation_description="Lista de desenvolvedores",
        responses={
            200: DeveloperSerializer(many=True)
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo desenvolvedor",
        request_body=DeveloperSerializer,
        responses={
            201: DeveloperSerializer,
            400: "Erro de validação nos dados fornecidos"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Detalhes do desenvolvedor",
        responses={
            200: DeveloperSerializer,
            404: "Desenvolvedor não encontrado"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza um desenvolvedor",
        request_body=DeveloperSerializer,
        responses={
            200: DeveloperSerializer,
            400: "Erro de validação nos dados fornecidos",
            404: "Desenvolvedor não encontrado"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta um desenvolvedor",
        responses={
            204: "Desenvolvedor deletado com sucesso",
            404: "Desenvolvedor não encontrado"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
