from django.urls import path
from .views import *

appName = "oficina"

urlpatterns = [
    path(
        'lista/',
        OficinaListView.as_view(),
        name='lista'
    ),
]