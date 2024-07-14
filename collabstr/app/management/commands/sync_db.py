# your_app/management/commands/populate_database.py
from django.core.management.base import BaseCommand
from app.scripts.populate_db import populate_db as populate_function

class Command(BaseCommand):
    help = 'Populates the database with initial data from JSON file'

    def handle(self, *args, **kwargs):
        populate_function()
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
