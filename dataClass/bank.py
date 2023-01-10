import random
from dataclasses import dataclass, field

"""
learned section: 
    -dataclasses are ducking nice to use 
    -have a simple more clear syntax than a normal class if you 
    want to stor just data

    -if you disable init you can still edit the values after it
    -it's interesting to work with declaration in python 
"""

def generateId() -> int:
    return random.randint(1000, 9999)

@dataclass(slots=True)
class Costumer:
    prename: str
    name: str
    money: str
    summ: list = field(init = False, repr = False)
    id: int = field(init = False, default_factory=generateId)

    def __post_init__(self) -> None:
        self.summ = [self.prename, self.name]

def main() -> None:
    person = Costumer(prename="Jeff", name="Smith", money = "31")
    person.id = 4331
    print(person)

if __name__ == '__main__':
    main()
