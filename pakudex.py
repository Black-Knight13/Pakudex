from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuris = []
        self.size = 0

    # Initializes this object as storing 0 pakuri, and to contain exactly capacity objects when completely full. The
    # default capacity for the pakudex should be 20

    def get_size(self):
        return self.size
    # Returns the number of critters currently being stored in the pakudex

    def get_capacity(self):
        return self.capacity
    # Returns the number of critters that the pakudex has the capacity to hold at most

    def get_species_array(self):
        res = []
        for name in self.pakuris:
            if len(self.pakuris) == 0:
                return None
            else:
                res.append(name.species)
        return res

    # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no species
    # added yet, this method should return None

    def get_stats(self, species):
        res = []
        for pakuri in self.pakuris:
            if pakuri.species == species:
                res.append(pakuri.species)
                return [pakuri.attack, pakuri.defense, pakuri.speed]
            else:
                return None

    # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
    # respectively; if species is not in the pakudex, returns None

    def sort_pakuri(self):
        self.pakuris.sort(key=lambda pakuri: pakuri.species)

    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name

    def add_pakuri(self, species):
        if species in self.get_species_array():
            return False
        elif self.size == self.capacity:
            return False
        else:
            self.pakuris.append(Pakuri(species))
            self.size += 1
            return True

    # Adds species to the pakudex; if successful, return True, and False otherwise

    def evolve_species(self, species):
        if species in self.get_species_array():
            for pakuri in self.pakuris:
                if pakuri.species == species:
                    Pakuri.evolve(pakuri)
                    return True
        else:
            return False

    # Attempts to evolve the corresponding Pakuri within the pakudex; if successful, return True, and False otherwise
