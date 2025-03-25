from rest_framework import routers
from organisation.viewset import OrganisationViewSet
from product.viewset import ProductViewSet, ProductTypeViewSet

router = routers.DefaultRouter()

router.register('organisation', OrganisationViewSet, basename="organisation")
router.register('product', ProductViewSet, basename="product")
router.register('product-type', ProductTypeViewSet, basename="product-type")