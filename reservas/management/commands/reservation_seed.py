from asyncio.log import logger
from django.core.management.base import BaseCommand
import random

from reservas.models import Reservation
from anuncios.models import Ad

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
    logger.info("Delete all instances")
    Reservation.objects.all().delete()


def create_reservation():
    logger.info("Creating reservation")

    Ads_code = Ad.objects.all()

    guests = [
        3,
        8,
        5,
        1,
        9
    ]
    comments = [
        "comantário 1",
        "comentário 2",
        "comentário 3",
        "comentário 4",
        "comentário 5"
    ]
    total_price = [
        15.85,
        25.89,
        46.57,
        73.51,
        2.99
    ]
    check_in = [
        '2022-11-15',
        '2022-11-04',
        '2022-11-07',
        '2002-11-18',
        '2022-11-27'
    ]
    check_out = [
        '2022-12-10',
        '2022-12-05',
        '2022-12-18',
        '2022-12-04',
        '2022-12-21'
    ]
    reservation = Reservation(
        ads_code=random.choice(Ads_code),
        guests=random.choice(guests),
        comments=random.choice(comments),
        total_price=random.choice(total_price),
        check_in=random.choice(check_in),
        check_out=random.choice(check_out),
    )
    reservation.save()
    logger.info("{} reservation created.".format(reservation))
    return reservation


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in range(8):
        create_reservation()
