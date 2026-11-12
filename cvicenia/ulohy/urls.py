from django.urls import path
from . import views

urlpatterns = [
    path('', views.ulohy, name='ulohy'),
    path('ahoj/', views.ahoj, name='ahoj'),
    path('o-mne/', views.o_mne, name='o_mne'),
    path('rozvrh/', views.rozvrh, name='rozvrh'),
]