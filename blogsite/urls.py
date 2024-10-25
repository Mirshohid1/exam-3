from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('privacy-policy/', views.PrivacyPolicyTemplateView.as_view(), name='privacy-policy'),
    path('terms-conditions/', views.TermsConditionsTemplateView.as_view(), name='terms-conditions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)