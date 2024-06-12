from rest_framework.routers import DefaultRouter
from wahrehouse.api.views import ProductViewSet

router = DefaultRouter() # enrutador base de la API
router.register("products", ProductViewSet, basename = "product")

urlpatterns = router.urls