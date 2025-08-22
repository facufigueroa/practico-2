from django.urls import path
from .views import *

appName = "persona"

urlpatterns = [
    path(
        'lista/',
        PersonaListView.as_view(),
        name='lista'
    ),
]