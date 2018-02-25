class Animal:
    """Animal class."""

    def __init__(self, genus, species):
        self.kingdom = 'Animalia'
        self.study = 'Zoology'
        self.genus = genus
        self.species = species
    
class Vertibrate(Animal):
    """Veribrate subclass of Animal"""
    def __init__(self, genus, species):
        Animal.__init__(self, genus, species)
        self.backbone = True

class Invertibrate(Animal):
    """Invertibrate subclass of Animal"""
    def __init__(self, genus, species):
        Animal.__init__(self, genus, species)
        self.backbone = False

# Vertibrates
class Fish(Vertibrate):
    """Fish subclass of Vertibrate."""
    def __init__(self, genus, species):
        Vertibrate.__init__(self, genus, species)

class Amphibian(Vertibrate):
    """Amphibian subclass of Vertibrate."""
    def __init__(self, genus, species):
        Vertibrate.__init__(self, genus, species)

class Reptile(Vertibrate):
    """Reptile subclass of Vertibrate."""
    def __init__(self, genus, species):
        Vertibrate.__init__(self, genus, species)
        self.body_cover = 'Scales'
        self.blood = 'Cold-blooded'
        self.lays_eggs = True

class Bird(Vertibrate):
    """Bird subclass of Vertibrate."""
    def __init__(self, genus, species):
        Vertibrate.__init__(self, genus, species)
        self.body_cover = 'Feathers'
        self.blood = 'Warm-blooded'
        self.lays_eggs = True

class Mammal(Vertibrate):
    """Mammal subclass of Vertibrate."""
    def __init__(self, genus, species):
        Vertibrate.__init__(self, genus, species)
        self.body_cover = 'Hair or Fur'
        self.blood = 'Warm-blooded'

class Arthropod(Invertibrate):
    def __init__(self, genus, species):
        self.phylum = 'Arthropoda'

class Insect(Arthropod):
    """Insect subclass of Arthropod."""
    def __init__(self, genus, species):
        Animal.__init__(self, genus, species)
        self.body_cover = 'Chitinous exoskeleton'
        self.body_parts = ['Head', 'Thorax', 'Abdomen']
        self.legs = 6
        self.antennae = True

class Crustacean(Arthropod):
    """Crustacean subclass of Arthropod."""
    def __init__(self, genus, species):
        Arthropod.__init__(self, genus, species)
        self.subphylum = 'Crustacea'

class Crab(Crustacean):
    """Crab subclass of Crustacean."""
    def __init__(self, genus, species):
        Crustacean.__init__(self, genus, species)
        self.order = 'Decapoda'
        self.suborder = 'Pleocyemata'
        self.infraorder = 'Brachyura'