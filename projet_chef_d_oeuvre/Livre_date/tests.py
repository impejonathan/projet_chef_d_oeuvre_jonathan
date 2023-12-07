# test.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Livre_date.forms import SignupForm

User = get_user_model()

@pytest.mark.django_db
def test_signup_valid_data(client):
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'Complex@1234',
        'password2': 'Complex@1234',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('index')
    user = User.objects.get(username='testuser')
    assert user is not None
    assert user.email == 'test@example.com'
    assert user.first_name == 'Test'
    assert user.last_name == 'User'

@pytest.mark.django_db
def test_signup_password_too_similar(client):
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'testuser1234',
        'password2': 'testuser1234',
    }
    response = client.post(url, data)
    assert response.status_code != 302  # La création de l'utilisateur ne doit pas réussir

@pytest.mark.django_db
def test_signup_password_too_short(client):
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'short',
        'password2': 'short',
    }
    response = client.post(url, data)
    assert response.status_code != 302  # La création de l'utilisateur ne doit pas réussir

@pytest.mark.django_db
def test_login_valid_user(client):
    # Création d'utilisateurs de test
    User.objects.create_user(username='impe.jonathan2', password='morganelechat')
    User.objects.create_user(username='impe.jonathan1', password='morganelechat')
    User.objects.create_user(username='impe.jonathan3', password='morganelechat')
    User.objects.create_user(username='impe.jonathan4', password='morganelechat')

    # Test de connexion avec des identifiants valides
    for i in range(1, 5):
        url = reverse('login')
        response = client.post(url, {'username': f'impe.jonathan{i}', 'password': 'morganelechat'})
        assert response.status_code == 302
        assert response.url == reverse('index')

@pytest.mark.django_db
def test_login_invalid_password(client):
    # Création d'un utilisateur de test
    User.objects.create_user(username='impe.jonathan2', password='morganelechat')

    # Test de connexion avec un mot de passe invalide
    url = reverse('login')
    response = client.post(url, {'username': 'impe.jonathan2', 'password': 'mauvaismdp'})
    assert response.status_code != 302  # La connexion ne doit pas réussir

@pytest.mark.django_db
def test_login_nonexistent_user(client):
    # Test de connexion avec un utilisateur inexistant
    url = reverse('login')
    response = client.post(url, {'username': 'utilisateur_inexistant', 'password': 'morganelechat'})
    assert response.status_code != 302  # La connexion ne doit pas réussir
