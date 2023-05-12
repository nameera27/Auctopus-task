from django.urls import path,include
from .router import router
from api import views

urlpatterns=[
    path('api/',include(router.urls)),
]