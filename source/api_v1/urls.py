from django.urls import path
from api_v1.views import add

app_name = "api_v1"

urlpatterns = [
    path("add/", add),
    path("subtract/", add),
    path("multiply/", add),
    path("divide/", add),
]