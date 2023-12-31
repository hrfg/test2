from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/router/', include(router.urls)),
    path('users/', views.UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('auth/', obtain_auth_token),
    path('auth/msg/', views.secureview),
    path('authJ/', include('djoser.urls')),
    path('authJ/', include('djoser.urls.authtoken'))
]
