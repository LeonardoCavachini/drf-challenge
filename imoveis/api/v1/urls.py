from rest_framework.routers import SimpleRouter

from .views import PropertyViewSet

router = SimpleRouter()
router.register('imoveis', PropertyViewSet)
