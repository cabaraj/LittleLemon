from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuItemTest(TestCase):

    def test_adding_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 80")

    def test_adding_booking(self):
        booking = Booking.objects.create(name='Peter', guests=2, date=datetime(2024,2,14))
        self.assertEqual(str(booking), "Peter (2)")