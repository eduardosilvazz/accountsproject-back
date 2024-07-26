from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from core.views import ProductViewSet, CategoryViewSet  

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
