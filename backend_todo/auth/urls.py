from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import registration_view, logout_view, getToken_view, CustomAuthToken


urlpatterns = [
  path('login/', CustomAuthToken.as_view(), name='login'),
  path('get-token/<str:auth_token>/', getToken_view, name='getToken'),
  path('register/', registration_view, name='register'),
  path('logout/', logout_view, name='logout'),

  # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
