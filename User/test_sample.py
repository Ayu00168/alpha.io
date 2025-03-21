import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def create_user_url():
    return reverse("create_user")
@pytest.fixture
def login_url():
    return reverse("login")

@pytest.mark.django_db
class TestClass:
    def test_create_user(self, create_user_url, api_client):
        requested_data = {
            "email": "r1@n.com",
            "password": "123456789",
            "first_name": "Rahul",
            "last_name": "Kumar",
            "phone": "1234567890"
        }

        
        response = api_client.post(create_user_url, requested_data, format="json")
        assert response.status_code == 201 
        
    def test_create_user_invalid(self, create_user_url, api_client):
        requested_data = {
            "email": ".com",
            "password": "123456789",
            "first_name": "Rahul",
            "last_name": "" ,
            "phone": "1234567890",
            }
        
        response = api_client.post(create_user_url, requested_data, format="json")
        assert response.status_code == 400

        data = response.json()
        
        assert "email" in data
        data["email"] == ["Enter a valid email address."]
        
        
    def test_login_user(self, login_url, api_client):
        requested_data = {
            "email": "r@n.com",
            "password": "1234500759",
            "first_name": "Rahul",
            "last_name": "Kumar",
            "phone": "1234567890"
        }
        
        response = api_client.post(login_url, requested_data, format="json")
        assert response.status_code == 201
            