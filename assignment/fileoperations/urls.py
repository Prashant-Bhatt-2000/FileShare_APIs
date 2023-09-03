from django.urls import path
from .views import FileUpload, GetFiles, DownloadFile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", FileUpload.as_view(), name='file_upload' ),
    path("getfiles/", GetFiles.as_view(), name="get_files"),
    path("downloadfile/<str:fileid>", DownloadFile.as_view(), name="download_files"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)