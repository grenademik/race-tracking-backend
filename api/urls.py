from django.urls import path
from .views import (
    RaceDataList, RaceDataDetail, RaceDataCreate, RaceDataUpdate, RaceDataDelete,
    RaceTimingList, RaceTimingDetail, RaceTimingCreate, RaceTimingUpdate, RaceTimingDelete,
    apiOverview
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', apiOverview, name='api-overview'),
    # RaceData URLs
    path('racedata-list/', RaceDataList.as_view(), name='racedata-list'),
    path('racedata-detail/<str:pk>/', RaceDataDetail.as_view(), name='racedata-detail'),
    path('racedata-create/', RaceDataCreate.as_view(), name='racedata-create'),
    path('racedata-update/<str:pk>/', RaceDataUpdate.as_view(), name='racedata-update'),
    path('racedata-delete/<str:pk>/', RaceDataDelete.as_view(), name='racedata-delete'),
    
    # RaceTiming URLs
    path('racetiming-list/', RaceTimingList.as_view(), name='racetiming-list'),
    path('racetiming-detail/<str:pk>/', RaceTimingDetail.as_view(), name='racetiming-detail'),
    path('racetiming-create/', RaceTimingCreate.as_view(), name='racetiming-create'),
    path('racetiming-update/<str:pk>/', RaceTimingUpdate.as_view(), name='racetiming-update'),
    path('racetiming-delete/<str:pk>/', RaceTimingDelete.as_view(), name='racetiming-delete'),
]
