from asyncio.log import logger
from django.core.management.base import BaseCommand
import random

from anuncios.models import Ad
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
    logger.info("Delete Ads instances")
    Ad.objects.all().delete()


def create_ads():
    logger.info("Creating Ads")
    property_code = Propertie.objects.all()

    platform_name = [
        'zapimoveis',
        'praedium',
        'viva real',
        'OLX',
        'imocasa'
    ]

    platform_tax = [
        3.85,
        8.46,
        5.91,
        1.25,
        9.73
    ]

    ad = Ad(
        property_code=random.choice(property_code),
        platform_name=random.choice(platform_name),
        platform_tax=random.choice(platform_tax),
    )
    ad.save()
    logger.info("{} ads created.".format(ad))
    return ad


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in range(3):
        create_ads()
