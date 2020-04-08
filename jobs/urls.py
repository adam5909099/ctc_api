from rest_framework import routers
from .views import JobViewSet

router = routers.SimpleRouter()
router.register(r'', JobViewSet)
urlpatterns = router.urls
