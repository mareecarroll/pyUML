"""
Utility to help draw a UML class diagram for a module.

At the moment it parses a single module looking for classes,
identifies parents and can output these as yUML format.

Todo:
- Support multiple modules inspection.
- Maybe try sorting the yUML entries so they appear 
in file in the order of class hierarchy. Note that this
has no effect on rendering the yUML.
"""
import sys
import inspect
from collections import namedtuple

UMLEntity = namedtuple('UMLEntity', 'parent subclass')
""" Lightweight named tuple for holding parent and subclass info."""

def get_entities(module_to_inspect):
    """
    Args:
        module_to_inspect (module)
    Returns:
        list of UMLEntity: the classes to diagram
    """
    entities = []
    for _, val in inspect.getmembers(module_to_inspect):
        if isinstance(val, type):
            parents = parents = val.__bases__
            parent = parents[0].__name__
            entity = UMLEntity(parent=parent, subclass=val.__name__)
            entities.append(entity)
    return entities

def to_yuml(entities):
    """
    Args:
        entities (list of UMLEntity): entities to draw
    """
    print('// {type:class}')
    for entity in entities:
        if entity.parent == 'object':
            # only print the subclass, we don't want 'object'
            # at the top everytime!
            print('[' + entity.subclass + ']')
        else:
            # ensure the hierarchy is captured
            print('[' + entity.parent + ']<-[' + entity.subclass + ']')

if __name__ == "__main__":
    to_yuml(get_entities(__import__(sys.argv[1])))