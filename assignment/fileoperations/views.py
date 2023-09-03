from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.http import FileResponse, HttpResponse
from .models import Files
from .serializers import FileSerializer
from .permissionclass import ClientUserPermission, OpsUserPermission

class FileUpload(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OpsUserPermission]
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        serializer = FileSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response({'message': 'Post Posted successfully', 'data': serializer.data})
        
        return Response({'message': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class GetFiles(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ClientUserPermission]
    def get(self, request): 
        files = Files.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response({'status': 200, 'data': serializer.data})
    

class DownloadFile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ClientUserPermission]
    def get(self, request, fileid):
        try:
            file = Files.objects.get(id=fileid)
        except Files.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        file_data = file.file.read()
        response = HttpResponse(file_data, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
        return response