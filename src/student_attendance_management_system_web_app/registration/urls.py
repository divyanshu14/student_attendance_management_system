from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
]
