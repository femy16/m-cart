from django.apps import apps
from django.test import TestCase
from .apps import BagConfig


class TestCartConfig(TestCase):

    def test_account_app(self):
        self.assertEqual("bag", BagConfig.name)
        self.assertEqual("bag", apps.get_app_config("bag").name)