from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status 
from django.contrib.auth import get_user_model
from .models import User


class OpsRegisterTestCase(APITestCase): 
    def test_ops_registration(self):
        url = reverse('register_ops')

        data = {
                "name": "test",
                "email": "test@test.com",
                "password": "password"
               }
        response = self.client.post(url, data, format='json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .serializer import OpsLoginSerializer, ClientLoginSerializer

User = get_user_model()

class OpsLoginSerializerTestCase(APITestCase):
    def test_valid_login(self):
        user = User.objects.create_user(email="test@example.com", password="testpassword", is_ops=True, is_verified=True)

        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        serializer = OpsLoginSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        validated_data = serializer.validated_data

        self.assertIn("message", validated_data)
        self.assertIn("username", validated_data)
        self.assertIn("access", validated_data)
        self.assertIn("refresh", validated_data)

        self.assertEqual(validated_data["message"], "Login successful.")

    def test_invalid_login(self):
        data = {
            "email": "test@example.com",
            "password": "wrongpassword", 
        }
        serializer = OpsLoginSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn("non_field_errors", serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0], "Incorrect email or password.")

    def test_missing_fields(self):
            data = {
                "email": "test@example.com",
            }
            serializer = OpsLoginSerializer(data=data)

            self.assertFalse(serializer.is_valid())

            self.assertIn("password", serializer.errors)
            self.assertEqual(serializer.errors["password"][0], "This field is required.")



class ClientRegisterTestCase(APITestCase): 
    def test_client_registration(self):
        url = reverse('client_register')

        data = {
                "name": "fake",
                "email": "prashant.bhatt.2020@asb.edu.in",
                "password": "password"
               }
        response = self.client.post(url, data, format='json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


User = get_user_model()

class ClientLoginSerializerTestCase(APITestCase):
    def test_valid_login(self):
        client = User.objects.create_user(email="test@example.com", password="testpassword", is_client=True, is_verified=True)

        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        serializer = ClientLoginSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        validated_data = serializer.validated_data

        self.assertIn("message", validated_data)
        self.assertIn("username", validated_data)
        self.assertIn("access", validated_data)
        self.assertIn("refresh", validated_data)

        self.assertEqual(validated_data["message"], "Login successful.")

    def test_invalid_login(self):
        data = {
            "email": "test@example.com",
            "password": "wrongpassword", 
        }
        serializer = OpsLoginSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn("non_field_errors", serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0], "Incorrect email or password.")

    def test_missing_fields(self):
            data = {
                "email": "test@example.com",
            }
            serializer = ClientLoginSerializer(data=data)

            self.assertFalse(serializer.is_valid())

            self.assertIn("password", serializer.errors)
            self.assertEqual(serializer.errors["password"][0], "This field is required.")

