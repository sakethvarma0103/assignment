import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignemnt.settings')

import django
django.setup()

import csv
from datetime import datetime
from event.models import Event

def import_data_from_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = Event(
                event_name=row['event_name'],
                city_name=row['city_name'],
                date=datetime.strptime(row['date'], '%Y-%m-%d').date(),
                time=datetime.strptime(row['time'], '%H:%M:%S').time(),
                latitude=float(row['latitude']),
                longitude=float(row['longitude'])
            )
            event.save()

# Example usage:
csv_file_path = 'Backend_assignment_gg_dataset - dataset.csv'
import_data_from_csv(csv_file_path)
