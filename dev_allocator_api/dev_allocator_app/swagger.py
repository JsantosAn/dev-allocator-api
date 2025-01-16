from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Developer Allocator",
        default_version='v1',
        description=(
            "Esta API foi desenvolvida para gerenciar a alocação de desenvolvedores em "
            "projetos de software, garantindo que as equipes sejam formadas de maneira "
            "eficiente e atendam às exigências técnicas dos projetos."
        ),    
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
schema_view.security_definitions = {
    'Bearer': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header',
        'description': 'Adicione "Bearer <seu_token_jwt>" ao campo Authorization',
    }
}
