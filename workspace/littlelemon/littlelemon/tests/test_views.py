from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from decimal import Decimal
from datetime import datetime

class MenuViewTest(TestCase):

    def setUp(self):
        # add few instances of the Menu model
        Menu.objects.create(title="Ice Cream", price=Decimal(80), inventory=100)
        Menu.objects.create(title="Raspado", price=Decimal(40), inventory=54)

        Booking.objects.create(name="Peter", guests=2, date=datetime(2024,2,14))


    def test_menu_getall(self):
        # retrieve all the Menu object added
        # retrieve items must serialized
        testing_items = Menu.objects.all()
        self.assertEqual(2, len(testing_items))

    def test_menu_serializer_validation(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        serialized_items = MenuSerializer(data=serialized_items.data, many=True)
        self.assertTrue(serialized_items.is_valid())
        

    def test_booking_getall(self):
        testing_items = Booking.objects.all()
        self.assertEqual(1, len(testing_items))

    def test_booking_serializer_validation(self):
        items = Booking.objects.all()
        serialized_items = BookingSerializer(items, many=True)
        serialized_items = BookingSerializer(data=serialized_items.data, many=True)
        self.assertTrue(serialized_items.is_valid())