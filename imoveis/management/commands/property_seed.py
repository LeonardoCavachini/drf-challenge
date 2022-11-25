from asyncio.log import logger
from django.core.management.base import BaseCommand
import random

from imoveis.models import Propertie

MODE_REFRESH = 'refresh'
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    logger.info("Delete Property instances")
    Propertie.objects.all().delete()


def create_property():
    logger.info("Creating properties")
    limit_guests = [
        3,
        8,
        5,
        1,
        9
    ]
    bathroom_quantity = [
        3,
        8,
        5,
        1,
        9
    ]
    accept_animal = [
        True,
        False,
        False,
        True,
        False
    ]
    housekeeping_price = [15.85, 25.89, 46.57, 73.51, 2.99]
    activate_date = [
        '2022-11-15',
        '2022-11-04',
        '2022-11-07',
        '2002-11-18',
        '2022-11-27'
    ]

    property = Propertie(
        limit_guests=random.choice(limit_guests),
        bathroom_quantity=random.choice(bathroom_quantity),
        accept_animal=random.choice(accept_animal),
        housekeeping_price=random.choice(housekeeping_price),
        activate_date=random.choice(activate_date),
    )
    property.save()
    logger.info("{} reservation created.".format(property))
    return property


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in range(5):
        create_property()
