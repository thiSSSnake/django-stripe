from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/items/", include("stripe_backend.stripe_app.urls")),
]
