from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .views import RaceAPI, RaceDataAPI, RaceTimingAPI

schema_view = get_schema_view(
    openapi.Info(
        title="Race Tracking API",
        default_version='v1',
        description=("API documentation for Race management with nested"
                     "RaceData and RaceTiming"),
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@racetracking.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

router = routers.SimpleRouter()
router.register('races', RaceAPI, basename='races')
router.register('runners', RaceDataAPI, basename='RaceData')
router.register('race-timings', RaceTimingAPI, basename='RaceTiming')

urlpatterns = [
    # Documentation URLs
    re_path(r'^docs(?P<format>\.json|\.yaml)/$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('', include(router.urls)),
]
