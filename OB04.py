from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."


class Axe(Weapon):
    def attack(self):
        return "Боец размахивается топором!"


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает оружие: {weapon.__class__.__name__}")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} безоружен!")


# Шаг 4: Класс Monster
class Monster:
    def __init__(self, name="Монстр"):
        self.name = name
        self.is_defeated = False

    def take_hit(self):
        self.is_defeated = True
        print(f"{self.name} побеждён!")


# Шаг 5: Бой
def battle(fighter: Fighter, monster: Monster):
    print("⚔️ Бой начинается!")
    fighter.attack()
    monster.take_hit()


# --- Пример использования ---
if __name__ == "__main__":
    # Создаём бойца и монстра
    hero = Fighter("Герой")
    goblin = Monster("Гоблин")

    # Боец выбирает меч
    hero.change_weapon(Sword())
    battle(hero, goblin)

    print("\n--- Новый бой ---\n")

    # Новый монстр
    orc = Monster("Орк")
    # Боец выбирает лук
    hero.change_weapon(Bow())
    battle(hero, orc)

    print("\n--- Новый бой с новым оружием (топор) ---\n")

    dragon = Monster("Дракон")
    hero.change_weapon(Axe())
    battle(hero, dragon)
