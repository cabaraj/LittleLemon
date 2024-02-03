from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from decimal import Decimal

class MenuViewTest(TestCase):

    def setUp(self):
        # add few instances of the Menu model
        Menu.objects.create(title="Ice Cream", price=Decimal(80), inventory=100)
        Menu.objects.create(title="Raspado", price=Decimal(40), inventory=54)

    def test_getall(self):
        # retrieve all the Menu object added
        # retrieve items must serialized
        testing_items = Menu.objects.all()
        self.assertEqual(2, len(testing_items))

    def test_serializer_validation(self):

        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        serialized_items = MenuSerializer(data=serialized_items.data, many=True)
        self.assertTrue(serialized_items.is_valid())
        