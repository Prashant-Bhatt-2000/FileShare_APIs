from django.urls import path
from .views import OpsRegister, OpsLogin, ClientRegister, ClientLogin, VerifyEmail

urlpatterns = [
    path("opsregister/", OpsRegister.as_view(), name='register_ops' ),
    path("opslogin/", OpsLogin.as_view(), name='ops_login'),
    path("clientregister/", ClientRegister.as_view(), name='client_register'),
    path("clientlogin/", ClientLogin.as_view(), name='client_login'),
    path("verifytoken/<str:token>/", VerifyEmail.as_view(), name='verify_email'),
]