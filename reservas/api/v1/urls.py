from rest_framework.routers import SimpleRouter

from .views import ReservationsViewSet

routerReservation = SimpleRouter()
routerReservation.register(
    'reservas',
    ReservationsViewSet,
    basename='reservas'
)
