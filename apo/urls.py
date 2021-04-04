from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("apos", views.ApoViewSet, "apos")

urlpatterns = router.urls
