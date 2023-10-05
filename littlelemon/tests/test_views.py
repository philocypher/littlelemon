from django.test import TestCase,client
from restaurant import views
import json 
from django.urls import reverse
from restaurant import models
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self):
        items = models.Menu.objects.all()
        self.menu = [json.dumps(item) for item in items]
        
        self.client = APIClient()
    def test_getall(self):
        response = self.client.get(reverse('restaurant:menu-list'))
        self.assertEqual(self.menu, response.data)