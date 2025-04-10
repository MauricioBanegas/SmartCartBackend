from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from apps.users.views import CustomUserView, DeactivateAccountView

urlpatterns = [
    path('me/custom/', CustomUserView.as_view(), name='custom-user'),
    path('deactivate/', DeactivateAccountView.as_view(), name='deactivate-account'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
]

# from django.urls import path
# from rest_framework_simplejwt.views import TokenBlacklistView
# from apps.users.views import RegisterView, UserView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('me/', UserView.as_view(), name='user-detail'),
    
#     # Rutas personalizadas de usuario
#     path('me/custom/', views.CustomUserView.as_view(), name='custom-user'),
#     path('deactivate/', views.DeactivateAccountView.as_view(), name='deactivate-account'),
    
#     # Blacklist manual de refresh token (logout seguro)
#     path('logout/', TokenBlacklistView.as_view(), name='logout'),
# ]
