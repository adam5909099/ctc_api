from rest_framework import routers
from .views import PositionViewSet, JobViewSet

router = routers.SimpleRouter()
router.register(r'jobs', JobViewSet)
router.register(r'positions', PositionViewSet)
urlpatterns = router.urls
