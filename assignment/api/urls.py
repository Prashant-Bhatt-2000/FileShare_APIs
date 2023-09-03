from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("files/", include('fileoperations.urls'))
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 