from django.urls import include, path
from rest_framework.routers import SimpleRouter
from product import viewsets

router = SimpleRouter()
router.register(r"", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
