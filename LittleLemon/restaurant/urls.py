from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuView.as_view(), name='menu-detail'),
]
