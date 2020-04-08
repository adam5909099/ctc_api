from rest_framework import routers
from .views import PositionViewSet

router = routers.SimpleRouter()
router.register(r'', PositionViewSet)
urlpatterns = router.urls
