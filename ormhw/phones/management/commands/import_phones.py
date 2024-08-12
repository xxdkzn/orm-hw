import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone = Phone(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True'
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))