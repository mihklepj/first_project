import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

fakegen = Faker()

def populate(n=10):
        for entry in range(n):
                fake_name = fakegen.name()

                SUBJECT_LIST = ['matemaatika', 'geograafia', 'liikumine', 'bioloogia', 'eesti keel', 'inglise keel',
                                'ajalugu']
                fake_subject = random.choices(SUBJECT_LIST)[0]
                print(f'{fake_name}, {fake_subject}')
                Teacher.objects.get_or_create(name=fake_name, subject=fake_subject)

populate()