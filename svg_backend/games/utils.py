from rest_framework.pagination import PageNumberPagination
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SVG Backend Service",
        default_version='v1',
        description="Game CRUD Operation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="tawa@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class SetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100