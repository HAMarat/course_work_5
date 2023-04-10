from unit import BaseUnit


class ArenaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, *kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Arena(metaclass=ArenaSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def next_round(self):
        if self.game_is_running:
            enemy_result = self.enemy.hit(self.player)
            result = self._check_hp()
            if result is not None:
                return result
            self.stamina_regeneration()
            return enemy_result

    def _check_hp(self):
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = "Ничья"
        elif self.player.hp > 0 >= self.enemy.hp:
            self.battle_result = "Победил игрок"
        else:
            self.battle_result = "Победил противник"

        return self._end_game

    def _end_game(self):
        self._instance = {}
        self.game_is_running = False
        return self.battle_result

    def stamina_regeneration(self):
        units = (self.player, self.enemy)

        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina

            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def player_hit(self):
        result = self.player.hit(self.enemy)
        turn_result = self.next_round()
        return f"{result}<br>{turn_result}"

    def player_use_skill(self):
        result = self.player.use_skill(self.enemy)
        turn_result = self.next_round()
        return f"{result}<br>{turn_result}"
