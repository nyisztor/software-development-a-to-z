class Pokemon:
    def __init__(self, name: str, max_armor: int, max_hit: int):
        self.name = name
        self.armor = max_armor
        self.hit_points = max_hit
        self._is_charging = False 
    
    def attack(self):
        print(f"{self.name} attacks")

    def defend(self):
        print(f"{self.name} defends itself")

    def _change_attack(self):
        print(f"{self.name} is changing attack type")

class ElectricPokemon(Pokemon):
    def wild_charge(self):
        print("Wild charge attack!")

class WaterPokemon(Pokemon):

    def __init__(self, name: str, max_armor: int, max_hit: int, speed: int):
        Pokemon.__init__(self, name, max_armor, max_hit)
        self.speed = speed

    def attack(self):
        print(f"{self.name} special attack!!!")

    def aqua_tail(self):
        print("Aqua tail attack!")

class FlyingPokemon(Pokemon):
    def dragon_ascent(self):
        print("Dragon ascent attack!")


pikachu = Pokemon("Pikachu", 100, 1000)
vaporeon = WaterPokemon("Vaporeon", 99, 1000, 20)
raichu = ElectricPokemon("Raichu", 98, 800)
togekiss = FlyingPokemon("Togekiss", 75, 1200)

pokemons = [pikachu, vaporeon, raichu, togekiss]

for pokemon in pokemons:
    pokemon.attack()
    