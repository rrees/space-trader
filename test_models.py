from models import Ship, Merchant


def test_creating_new_trader():
    starting_ship = Ship(40, 7)

    merchant = Merchant(1000, starting_ship)
