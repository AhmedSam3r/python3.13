from dataclasses import dataclass


class Worker:
    def __init__(self):
        self.id = 0
        self.info = "Worker"


class Employee(Worker):
    def __init__(self, first_name: str, last_name: str, salary: int):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount: int = 5000) -> int:
        self.bonus += amount
        return self.bonus


@dataclass
class Boss:
    first_name: str
    last_name: str

    def give_raise(self, amount: int) -> int:
        self.bonus += amount
        return self.bonus


def main() -> None:
    print(Worker.__static_attributes__)
    # it prints tuple of attributes
    # ('first_name', 'last_name', 'salary')
    print(Employee.__static_attributes__)
    e = Employee("Ahmed", "Fekry", "2000")
    print(f"ID={e.id}, full name={e.first_name + " " + e.last_name}")
    # prints empty tuple
    print(Boss.__static_attributes__)


if __name__ == '__main__':
    main()
