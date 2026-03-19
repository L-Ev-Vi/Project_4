from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login/", views.MyLogin.as_view(), name="login"),
    path("logout/", views.MyLogout.as_view(), name="logout"),
    path("register/", views.CreateUser.as_view(), name="register"),
    path("email-confirm/<str:token>/", views.email_verification, name="email-confirm"),
    path("verification/", views.Verification.as_view(), name="verification"),
    path("edit_profile/", views.UpdateUser.as_view(), name="edit_profile"),
    path("password/", views.PasswordsChangeUser.as_view()),
]
