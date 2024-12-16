from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TheaterAvailabilityViewSet, CustomUnavailabilityViewSet, AvailableSlotsViewSet

router = DefaultRouter()
router.register(r'theatres/(?P<pk>\d+)/availability', TheaterAvailabilityViewSet, basename='theater-availability')
router.register(r'theatres/(?P<pk>\d+)/custom-unavailability', CustomUnavailabilityViewSet, basename='custom-unavailability')
router.register(r'theatres/(?P<pk>\d+)/slots', AvailableSlotsViewSet, basename='available-slots')

urlpatterns = [
    path('api/', include(router.urls)),
]
