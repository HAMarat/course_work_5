import json
from dataclasses import dataclass
from random import uniform
import marshmallow_dataclass


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:
    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name):
        for weapon in self.equipment.weapon:
            if weapon == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name):
        for armor in self.equipment.armor:
            if armor == armor_name:
                return armor
        return None

    def get_weapon_names(self):
        return [weapon.name for weapon in self.equipment.weapon]

    def get_armor_names(self):
        return [armor.name for armor in self.equipment.armor]

    def _get_equipment_data(self):
        with open('./data/equipment.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)
