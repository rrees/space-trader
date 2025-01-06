from collections import namedtuple
from dataclasses import dataclass

Merchant = namedtuple("Merchant", ["credits", "ship"])


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Ship:
    cargo_capacity: int
    jump_fuel_capacity: int


@dataclass
class Planet:
    id: str
    name: str
    location: Point
    tech_level: int


Cargo = namedtuple("Cargo", ["name", "quantity"])

Galaxy = namedtuple("Galaxy", ["seed", "size"])
