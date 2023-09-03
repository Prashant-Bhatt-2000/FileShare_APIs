from rest_framework import serializers
from .models import Files

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

        def validate(self, data):
            user = data.get('user')
            title = data.get('title')
            description = data.get('description')
            file = data.get('file')

            if not user:
                raise serializers.ValidationError('User is not available')

            if not title or not description:
                raise serializers.ValidationError("Please enter title and description")

            if not user.is_ops:
                raise serializers.ValidationError('You are not authorized to upload files.')
            
            
            if not user.is_verified:
                raise serializers.ValidationError('You are not a verified to perform any action. Please verify the email.')

            if file:
                file_name = file.name.lower()
                if not file_name.endswith(('.pptx', '.docx', '.xlsx')):
                    raise serializers.ValidationError('Only .pptx, .docx and .xlsx files are allowed.')

            return data