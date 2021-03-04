from rest_framework.routers import DefaultRouter
from .views import MemberCRUDViewSet, ActivityPeriodCRUDViewSet


router = DefaultRouter()
router.register('member', MemberCRUDViewSet)
router.register('activity-period', ActivityPeriodCRUDViewSet)

urlpatterns = router.urls
