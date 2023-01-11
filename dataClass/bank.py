import random
from dataclasses import dataclass, field

"""
learned section: 
    -dataclasses are ducking nice to use 
    -have a simple more clear syntax than a normal class if you 
    want to stor just data

    -if you disable init you can still edit the values after it
    -it's interesting to work with declaration in python 

    -you can define the standard value of print(obj)
        -->def __str__(self) -> str:
"""

def generateId() -> int:
    return random.randint(1000, 9999)

@dataclass(slots=True)
class Costumer:
    prename: str
    name: str
    money: int
    summ: list = field(init = False, repr = False)
    id: int = field(init = False, default_factory=generateId)

    def __post_init__(self) -> None:
        self.summ = [self.prename, self.name]

@dataclass(slots=True)
class costumerList:
    costumerList: list

class Bank: 
    def __init__(self, costumers : costumerList) -> None:
        self.costumerlist = costumers
        self.money = self.money()
    
    def money(self) -> int:
        money = 0
        print(money)
        for costumer in self.costumerlist.costumerList:
            money += costumer.money

        return money

    def __str__(self) -> str:
        return f"Combined we have {self.money}€"

def main() -> None:
    Jeff = Costumer(prename="Jeff", name="Smith", money = 31)
    Alison = Costumer(prename="Alison", name="Rupert", money = 498)
    Bob = Costumer(prename="Bob", name="Rupert", money = 321)

    saveFile = costumerList(costumerList=[Jeff, Alison, Bob])

    bankingBank = Bank(saveFile)

    print(bankingBank)

if __name__ == '__main__':
    main()
