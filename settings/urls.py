
from django.contrib import admin
from django.urls import path, include
from imoveis.api.v1.urls import router
from reservas.api.v1.urls import routerReservation

urlpatterns = [
    path('api/v1/', include('anuncios.api.v1.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('accounts.api.v1.urls')),
    path('api/v1/', include(routerReservation.urls)),
    path('admin/', admin.site.urls),
]
