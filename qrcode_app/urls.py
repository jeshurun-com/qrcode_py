from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.generate_qr, name='index'),
    path('manage/', views.manage_qr_codes, name='manage_qr_codes')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)