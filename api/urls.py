from django.urls import path, re_path
from .views import (
    RaceList, RaceDetail, RaceCreate, RaceUpdate, RaceDelete,
    RaceDataDetail, RaceDataCreate, RaceDataUpdate, RaceDataDelete,
    RaceTimingDetail, RaceTimingCreate, RaceTimingUpdate, RaceTimingDelete,
    apiOverview, RaceDataUpload
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Race Tracking API",
      default_version='v1',
      description="API documentation for Race management with nested RaceData and RaceTiming",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@racetracking.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Documentation URLs
    re_path(r'^docs(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API Overview
    path('', apiOverview, name='api-overview'),

    # Race URLs
    path('races/', RaceList.as_view(), name='race-list'),
    path('races/<str:pk>/', RaceDetail.as_view(), name='race-detail'),
    path('races/create/', RaceCreate.as_view(), name='race-create'),
    path('races/update/<str:pk>/', RaceUpdate.as_view(), name='race-update'),
    path('races/delete/<str:pk>/', RaceDelete.as_view(), name='race-delete'),

    # Nested RaceData URLs within a specific Race
    path('races/<str:race_pk>/data/create/', RaceDataCreate.as_view(), name='racedata-create'),
    path('races/<str:race_pk>/data/<str:pk>/', RaceDataDetail.as_view(), name='racedata-detail'),
    path('races/<str:race_pk>/data/update/<str:pk>/', RaceDataUpdate.as_view(), name='racedata-update'),
    path('races/<str:race_pk>/data/delete/<str:pk>/', RaceDataDelete.as_view(), name='racedata-delete'),

    # RaceTiming URLs directly linked to Race
    path('races/<str:race_pk>/timings/create/', RaceTimingCreate.as_view(), name='racetiming-create'),
    path('races/<str:race_pk>/timings/<str:pk>/', RaceTimingDetail.as_view(), name='racetiming-detail'),
    path('races/<str:race_pk>/timings/update/<str:pk>/', RaceTimingUpdate.as_view(), name='racetiming-update'),
    path('races/<str:race_pk>/timings/delete/<str:pk>/', RaceTimingDelete.as_view(), name='racetiming-delete'),
        path('races/<str:race_pk>/data/upload/', RaceDataUpload.as_view(), name='racedata-upload'),

]
