from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self):
        return self.stamina <= self.user.stamina

    def use(self, user, target):
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} пытался использовать {self.name}, но у него не хватило выносливости"


class FuryPunch(Skill):
    name = "Свирепый пинок"
    stamina = 6
    damage = 12

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."


class PowerfulThrust(Skill):
    name = "Мощный укол"
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."
