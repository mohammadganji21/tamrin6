class Soldier:
    soldier_ids = []

    def __init__(self, soldier_type, soldier_id, x, y):
        self.soldier_type = soldier_type
        self.soldier_id = soldier_id
        self.health = 100
        self.x = x
        self.y = y
        Soldier.soldier_ids.append(soldier_id)


class Archer(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("archer", soldier_id, x, y)


class Melee(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("melee", soldier_id, x, y)


class Game:
    def __init__(self, n):
        self.positions = {0: {}, 1: {}}
        self.players = {0: [], 1: []}
        self.current_turn = 0
        self.n = n

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn  # Toggle between 0 and 1

    def create_soldier(self, soldier_type, soldier_id, x, y):
        if soldier_id in [i.soldier_id for i in self.players[self.current_turn]]:
            print("duplicate tag")
            return

        if (x, y) not in self.positions[self.current_turn]:
            self.positions[self.current_turn][(x, y)] = []

        if soldier_type == "archer":
            soldier = Archer(soldier_id, x, y)
        elif soldier_type == "melee":
            soldier = Melee(soldier_id, x, y)
