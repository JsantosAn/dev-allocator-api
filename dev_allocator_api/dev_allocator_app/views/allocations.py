from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from ..models import Allocation
from ..serializers import AllocationSerializer

class AllocationViewSet(ModelViewSet):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all allocations",
        responses={200: AllocationSerializer(many=True)}
    )
    def list(self, request):
        allocations = Allocation.objects.all()
        serializer = AllocationSerializer(allocations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new allocation",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'project': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="ID do projeto",
                    example=1
                ),
                'developer': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="ID do desenvolvedor",
                    example=1
                ),
                'hours': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Horas alocadas",
                    example=40
                )
            },
            required=['project', 'developer', 'hours']
        ),
        responses={
            201: AllocationSerializer,
            400: "Erro de validação nos dados fornecidos"
        }
    )
    def create(self, request):
        serializer = AllocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific allocation",
        responses={
            200: AllocationSerializer,
            404: "Alocação não encontrada"
        }
    )
    def retrieve(self, request, pk=None):
        try:
            allocation = Allocation.objects.get(pk=pk)
        except Allocation.DoesNotExist:
            raise NotFound("Alocação não encontrada.")
        serializer = AllocationSerializer(allocation)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update an existing allocation",
        request_body=AllocationSerializer,
        responses={
            200: AllocationSerializer,
            400: "Erro de validação nos dados fornecidos",
            404: "Alocação não encontrada"
        }
    )
    def update(self, request, pk=None):
        try:
            allocation = Allocation.objects.get(pk=pk)
        except Allocation.DoesNotExist:
            raise NotFound("Alocação não encontrada.")
        serializer = AllocationSerializer(allocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific allocation",
        responses={
            204: "Alocação excluída com sucesso",
            404: "Alocação não encontrada"
        }
    )
    def destroy(self, request, pk=None):
        try:
            allocation = Allocation.objects.get(pk=pk)
        except Allocation.DoesNotExist:
            raise NotFound("Alocação não encontrada.")
        allocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
