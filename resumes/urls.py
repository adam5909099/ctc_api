from rest_framework import routers
from .views import PositionViewSet

router = routers.SimpleRouter()
router.register(r'positions', PositionViewSet)
urlpatterns = router.urls
