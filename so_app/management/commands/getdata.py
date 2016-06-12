from django.core.management.base import BaseCommand
from so_app.script import StackExchangeInfo


class Command(BaseCommand):
    help = "Get data and update models"

    def handle(self, *args, **options):
        try:
            so = StackExchangeInfo()
            so.get_tag_info()
        except Exception as e:
            raise e
