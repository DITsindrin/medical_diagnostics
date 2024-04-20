from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verification_account, ActivationCompleted, \
    ActivationFailed, UserListView, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('verify/<str:uidb64>/', verification_account, name='email_verification'),
    path('verification_completed', ActivationCompleted.as_view(), name='verification_completed'),
    path('verification-failed', ActivationFailed.as_view(), name='verification_failed'),
    path('user-list/', UserListView.as_view(), name='user-list'),

]
