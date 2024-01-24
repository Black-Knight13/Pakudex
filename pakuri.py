class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
    # Initialize the pakuri object with species attribute
    def get_species(self):
        return self.species
    # Returns the species of this critter

    def get_attack(self):
        return self.attack

    # Returns the attack value for this critter

    def get_defense(self):
        return self.defense

    # Returns the defense value for this critter
    def get_speed(self):
        return self.speed

    # Returns the speed of this critter

    def set_attack(self, new_attack):
        self.attack = new_attack

    # Changes the attack value for this critter to new_attack
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    # Will evolve the critter as follows: a) double the attack (multiply by 2); b) quadruple the defense (multiply by
    # 4); and c) triple the speed (multiply by 3).
