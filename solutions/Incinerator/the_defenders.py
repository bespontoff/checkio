#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run the-defenders

# In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additionaldefenseparameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
# The basic parameters of the Defender:
# health = 60
# attack = 3
# defense = 2
# 
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:3 types of units
# 
# 
# END_DESC

# Taken from mission Army Battles

# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.is_alive = True
        self.health = 50
        self.attack = 5

    def damage(self, attack):
        self.health -= attack


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def damage(self, attack):
        if attack > self.defense:
            self.health -= attack - self.defense


def fight(unit_1, unit_2, unit_1_attack=True):
    unit_1_attack = unit_1_attack
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1_attack:
            unit_2.damage(unit_1.attack)
            if unit_2.health <= 0: unit_2.is_alive = False
            unit_1_attack = False
        else:
            unit_1.damage(unit_2.attack)
            if unit_1.health <= 0: unit_1.is_alive = False
            unit_1_attack = True
    return True if unit_1.is_alive else False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for _ in range(count):
            self.units.append(unit())

    def is_defeat(self):
        for unit in self.units:
            if unit.is_alive: return False
        return True


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
                if army_2.is_defeat(): return True
                black = army_2.units.pop(0)
            else:
                army_1.units.append(white)
                if army_1.is_defeat(): return False
                white = army_1.units.pop(0)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")