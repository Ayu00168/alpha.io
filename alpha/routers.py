from rest_framework import routers
from organisation.viewset import OrganisationViewSet

router = routers.DefaultRouter()

router.register('organisation', OrganisationViewSet, basename="organisation")