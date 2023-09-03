from django.test import TestCase
from accounts.models import User
from .models import Files
from .serializers import FileSerializer


class FilesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword", is_ops=True, is_verified=True)

    def testcase_create_file(self):
        file_data = Files.objects.create(
            user=self.user,
            file='testfile.txt',
            title='Test File',
            description='This is a test file.'
        )

        self.assertEqual(file_data.user, self.user)
        self.assertEqual(file_data.file, 'testfile.txt')
        self.assertEqual(file_data.title, 'Test File')
        self.assertEqual(file_data.description, 'This is a test file.')


    def testcase_without_title(self):
        data = {
            'user': self.user,
            'file': 'testfile.txt',
            'description': 'This is a test file.'
        }

        serializer = FileSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
        self.assertEqual(serializer.errors["title"][0], "This field is required.")



    def testcase_without_user(self):
        data = {
            'file': 'File.txt',
            'title': 'Title',
            'description': 'description of topic' 
        }

        serializer = FileSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn("user", serializer.errors)
        self.assertEqual(serializer.errors["user"][0], "This field is required.")

    
    def testcase_without_description(self):
        data = {
            'user': self.user,
            'file': 'File.txt',
            'title': 'Title', 
        }

        serializer = FileSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn("description", serializer.errors)
        self.assertEqual(serializer.errors["description"][0], "This field is required.")