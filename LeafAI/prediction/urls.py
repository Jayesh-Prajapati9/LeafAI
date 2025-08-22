from django.urls import path
from .views import predict_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("", predict_view, name="predict"),
]
