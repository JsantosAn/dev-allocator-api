from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from ..models import Project
from ..serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Nome do projeto",
                    example="Desenvolvimento de API"
                ),
                'start_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATE,
                    description="Data de início do projeto",
                    example="2025-01-01"
                ),
                'end_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATE,
                    description="Data de término do projeto",
                    example="2025-12-31"
                ),
                'Technologies': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="IDs das tecnologias associadas ao projeto",
                    example=[1, 2, 3]
                ),
            },
            required=['name', 'start_date', 'end_date', 'Technologies']
        ),
        responses={
            201: openapi.Response(description="Projeto criado com sucesso", schema=ProjectSerializer),
            400: "Erro de validação nos dados fornecidos"
        }
    )
    def create(self, request, *args, **kwargs):
      
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Nome do projeto",
                    example="Desenvolvimento de API"
                ),
                'start_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATE,
                    description="Data de início do projeto",
                    example="2025-01-01"
                ),
                'end_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATE,
                    description="Data de término do projeto",
                    example="2025-12-31"
                ),
                'Technologies': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="IDs das tecnologias associadas ao projeto",
                    example=[1, 2, 3]
                ),
            },
            required=['name', 'start_date', 'end_date', 'Technologies']
        ),
        responses={
            200: openapi.Response(description="Projeto atualizado com sucesso", schema=ProjectSerializer),
            404: "Projeto não encontrado",
            400: "Erro de validação nos dados fornecidos"
        }
    )
    def update(self, request, *args, **kwargs):
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)