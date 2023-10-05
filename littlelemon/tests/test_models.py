from django.test import TestCase
from restaurant import models

class MentTest(TestCase):
    def test_create_item(self):
        item = models.Menu.objects.create(title='icecream', price=100, inventory=10)
        self.assertEqual(str(item), 'icecream : 100') 
