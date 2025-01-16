from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models import Technology
from ..serializers import TechnologySerializer

class TechnologyViewSet(viewsets.ModelViewSet):

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        operation_description="Create a new technology",
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_FORM,
                description="Name of the technology to be created",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            201: openapi.Response(
                description="Technology created successfully",
                schema=TechnologySerializer
            ),
            400: "Validation error"
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve a list of all technologies",
        responses={200: TechnologySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a technology by its ID",
        responses={200: TechnologySerializer, 404: "Not Found"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a technology",
        request_body=TechnologySerializer,
        responses={
            200: openapi.Response(
                description="Technology updated successfully",
                schema=TechnologySerializer
            ),
            404: "Not Found",
            400: "Validation error"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a technology",
        responses={204: "No Content", 404: "Not Found"}
    )
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Technology.DoesNotExist:
            return Response({"error": "Technology not found"}, status=status.HTTP_404_NOT_FOUND)
