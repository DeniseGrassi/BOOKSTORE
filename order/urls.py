#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework import routers
from order import viewsets

router = routers.SimpleRouter()
router.register(r"", viewsets.OrderViewSet, basename="order")  # <- sem 'order' aqui

urlpatterns = [
    path("", include(router.urls)),
]
