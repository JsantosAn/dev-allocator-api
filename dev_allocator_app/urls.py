from django.urls import path, include
from .views import technologies, developers, projects, allocations, autenticacao
from dev_allocator_app.swagger import schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', projects.ProjectViewSet)
router.register(r'developers', developers.DeveloperViewSet)
router.register(r'technologies', technologies.TechnologyViewSet)
router.register(r'allocations', allocations.AllocationViewSet)


urlpatterns = [
    
    path('token/', autenticacao.CustomTokenObtainPairView.as_view()),
    path('token/refresh/', autenticacao.CustomTokenRefreshView.as_view() ),
    path('', include(router.urls)),  
]


