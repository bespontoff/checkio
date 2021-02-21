#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run the-warlords

# 
# END_DESC

# Taken from mission The Weapons

class Warrior:
    def __init__(self):
        self.is_alive = True
        self.health = 50
        self.max_health = self.health
        self.attack = 5
        self.army = None

    def damage(self, attack):
        self.health -= attack
        return attack

    def hit(self, unit):
        unit.damage(self.attack)
        self.heal_me()

    def heal_me(self):
        if self.army is not None and len(self.army.units):
            if self.army.units[0].__class__.__name__ == "Healer":
                self.army.units[0].heal(self)

    def equip_weapon(self, weapon):
        self.max_health += weapon.health
        self.health += weapon.health
        if self.health <= 0:
            self.is_alive = False
        self.attack += weapon.attack
        if self.attack < 0:
            self.attack = 0


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__()
        self.health = 60
        self.max_health = self.health
        self.attack = 3
        self.defense = 2

    def damage(self, attack):
        if attack > self.defense:
            self.health -= attack - self.defense
        return attack - self.defense

    def equip_weapon(self, weapon):
        super(Defender, self).equip_weapon(weapon)
        self.defense += weapon.defence
        if self.defense < 0:
            self.defense = 0


class Vampire(Warrior):
    def __init__(self):
        super(Vampire, self).__init__()
        self.health = 40
        self.max_health = self.health
        self.attack = 4
        self.vampirism = 50  # in percents

    def hit(self, unit):
        dmg = unit.damage(self.attack)
        self.health += dmg * (self.vampirism / 100)
        if self.health > self.max_health:
            self.health = self.max_health
        self.heal_me()

    def equip_weapon(self, weapon):
        super(Vampire, self).equip_weapon(weapon)
        self.vampirism += weapon.vampirism
        if self.vampirism < 0:
            self.vampirism = 0


class Lancer(Warrior):
    def __init__(self):
        super(Lancer, self).__init__()
        self.attack = 6

    def hit(self, unit):
        unit.damage(self.attack)
        if unit.army:
            unit.army.units[0].damage(self.attack * 0.5)
        self.heal_me()


class Healer(Warrior):
    def __init__(self):
        super(Healer, self).__init__()
        self.health = 60
        self.max_health = self.health
        self.attack = 0
        self.heal_power = 2

    def heal(self, unit):
        if self.is_alive:
            unit.health += self.heal_power
            if unit.health > unit.max_health:
                unit.health = unit.max_health

    def equip_weapon(self, weapon):
        super(Healer, self).equip_weapon(weapon)
        self.heal_power += weapon.heal_power
        if self.heal_power < 0:
            self.heal_power = 0


class Warlord(Warrior):
    def __init__(self):
        super(Warlord, self).__init__()
        self.health = 100
        self.max_health = self.health
        self.attack = 4
        self.defense = 2

    def equip_weapon(self, weapon):
        super(Warlord, self).equip_weapon(weapon)
        self.defense += weapon.defence
        if self.defense < 0:
            self.defense = 0


class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defence = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(5, 2, 0, 0, 0)


class Shield(Weapon):
    def __init__(self):
        super(Shield, self).__init__(20, -1, 2, 0, 0)


class GreatAxe(Weapon):
    def __init__(self):
        super(GreatAxe, self).__init__(-15, 5, -2, 10, 0)


class Katana(Weapon):
    def __init__(self):
        super(Katana, self).__init__(-20, 6, -5, 50, 0)


class MagicWand(Weapon):
    def __init__(self):
        super(MagicWand, self).__init__(30, 3, 0, 0, 3)


def fight(unit_1, unit_2, unit_1_attack=True):
    unit_1_attack = unit_1_attack

    while unit_1.is_alive and unit_2.is_alive:

        if unit_1_attack:
            unit_1.hit(unit_2)
            if unit_2.health <= 0:
                unit_2.is_alive = False
            unit_1_attack = False
        else:
            unit_2.hit(unit_1)
            if unit_1.health <= 0:
                unit_1.is_alive = False
            unit_1_attack = True

    return True if unit_1.is_alive else False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for _ in range(count):
            soldier = unit()
            soldier.army = self
            if type(soldier) == Warlord:
                if not self.have_warlord():
                    self.units.append(soldier)
            else:
                self.units.append(soldier)

    def is_defeat(self):

        for unit in self.units:
            if unit.is_alive:
                return False
        return True

    def get_live_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit
        return False

    def have_warlord(self):
        for unit in self.units:
            if type(unit) == Warlord:
                return True
        return False

    def move_units(self):
        if self.have_warlord():
            print('warlord in units')


class Battle:
    def __init__(self):
        pass

    def fight(self, army_1, army_2):
        white = army_1.units.pop(0)
        black = army_2.units.pop(0)
        while True:
            white_win = fight(white, black)
            if white_win:
                army_2.units.append(black)
                if army_2.is_defeat():
                    return True
                black = army_2.units.pop(0)
            else:
                army_1.units.append(white)
                if army_1.is_defeat():
                    return False
                white = army_1.units.pop(0)

    def straight_fight(self, army_1, army_2):

        while True:
            if army_1.is_defeat():
                return False
            if army_2.is_defeat():
                return True

            fight(army_1.get_live_unit(), army_2.get_live_unit())
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ronald = Warlord()
	heimdall = Knight()

	fight(heimdall, ronald) == False

	my_army = Army()
	my_army.add_units(Warlord, 1)
	my_army.add_units(Warrior, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 2)

	enemy_army = Army()
	enemy_army.add_units(Warlord, 3)
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 2)
	enemy_army.add_units(Knight, 2)

	my_army.move_units()
	enemy_army.move_units()

	type(my_army.units[0]) == Lancer
	type(my_army.units[1]) == Healer
	type(my_army.units[-1]) == Warlord

	type(enemy_army.units[0]) == Vampire
	type(enemy_army.units[-1]) == Warlord
	type(enemy_army.units[-2]) == Knight

	#6, not 8, because only 1 Warlord per army could be
	len(enemy_army.units) == 6

	battle = Battle()

	battle.fight(my_army, enemy_army) == True
    print("Coding complete? Let's try tests!")