from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what-is/', views.what_is, name='what_is'),
    path('law-enforcement/', views.law_enforcement, name='law_enforcement'),
    path('enforcer/', views.enforcer, name='enforcer'),
    path('hotline/', views.hotline, name='hotline'),
    path('contact/', views.contact, name='contact'),
    path('safety-check/', views.safety_check, name='safety_check'),
]