from django.urls import include, path
from rest_framework.routers import SimpleRouter
from product import viewsets

router = SimpleRouter()
router.register(r"products", viewsets.ProductViewSet, basename="product")
router.register(r"categories", viewsets.CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]

