from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from Avtoapi.views import CustomerViewSet, AdvertsViewSet, ProductViewSet, GetProductView, GetUserView

router = DefaultRouter()
router.register('adverts', AdvertsViewSet)
router.register('product', ProductViewSet)
router.register('customer', CustomerViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/customer-filter/', GetUserView.as_view()),
    path('api/product-filter/', GetProductView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
