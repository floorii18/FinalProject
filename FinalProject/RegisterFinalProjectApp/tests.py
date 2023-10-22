from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from BaseFinalProjectApp.forms import *

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
class ContactPageTest(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        
class MessagesPageTest(TestCase):
    def test_messages_page_for_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('messages'))
        self.assertEqual(response.status_code, 200)
        
    def test_messages_page_for_unauthenticated_user(self):
        response = self.client.get(reverse('messages'))
        self.assertEqual(response.status_code, 302)