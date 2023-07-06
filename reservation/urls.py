from django.urls import path
from . import views
from .views import menuView, bookingView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuView.as_view()),
    path('booking/', bookingView.as_view()),
    path('users/', views.UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
