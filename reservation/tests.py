from django.test import TestCase
from .models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="test item", price=7.77, inventory=3)
        itemstr = item.__str__()

        self.assertEqual(itemstr, "ID:1 - test item")
