from collections import namedtuple
from dataclasses import dataclass

Merchant = namedtuple("Merchant", ["credits", "ship"])


@dataclass
class Ship:
    cargo_capacity: int
    jump_fuel_capacity: int


Cargo = namedtuple("Cargo", ["name", "quantity"])

Galaxy = namedtuple("Galaxy", ["seed"])
