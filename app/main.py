class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    persons: list[Person] = []

    for data in people:
        persons.append(Person(data["name"], data["age"]))

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data:
            if data["wife"] is not None:
                person.wife = Person.people[data["wife"]]

        if "husband" in data:
            if data["husband"] is not None:
                person.husband = Person.people[data["husband"]]

    return persons
