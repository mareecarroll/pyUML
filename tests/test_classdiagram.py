from classdiagram import get_entities
from classdiagram import UMLEntity
import animal

def test_get_entities():
    """Unit tests for get_entities.

    At the moment it is using animal.py but needs better than that

    Pretty crude testing at that
    """
    entities = get_entities(animal)
    assert len(entities) == 12, "Unexpected number of entities found"
    assert all(isinstance(x, UMLEntity) for x in entities), "Expecting all entities to be of type UMLEntity"
    assert len([x.parent == 'object' for x in entities]), "Expecting only one root class"

def test_mammal_is_vertibrate():
    """Test mammal is vertibrate."""
    entities = get_entities(animal)
    for entity in entities:
        if entity.subclass == 'Mammal':
            assert entity.parent == 'Vertibrate', "Expecting Mammal to be subclass of Vertibrate"