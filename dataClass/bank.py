import random
from dataclasses import dataclass, field

@dataclass(slots=True)
class Costumer:
    prename: str
    name: str
    money: str = "3"
    aktive: bool = True
    id: int = field(default_factory = random.randint(1000, 9999))

def main() -> None:
    person = Costumer(prename="Jeff", name="Smith", money = "31")
    print(person)

if __name__ == '__main__':
    main()
