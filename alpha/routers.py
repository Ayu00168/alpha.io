from rest_framework import routers
from organisation.viewset import OrganisationViewSet
from product.viewset import ProductViewSet, ProductTypeViewSet
from order.viewset import OrderViewSet, TableViewSet

router = routers.DefaultRouter()

router.register('organisation', OrganisationViewSet, basename="organisation")
router.register('product', ProductViewSet, basename="product")
router.register('product-type', ProductTypeViewSet, basename="product-type")
router.register('order', OrderViewSet, basename="order")
router.register('table', TableViewSet, basename="table")