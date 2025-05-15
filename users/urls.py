from django.urls import path
from .views import RegisterView, LogoutView, IsAuthenticatedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('is_authenticated/', IsAuthenticatedView.as_view()),
]
