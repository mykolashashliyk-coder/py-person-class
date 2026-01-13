class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list[dict]) -> list[Person]:
    persons = []
    for p in people:
        person = Person(p["name"], p["age"])
        persons.append(person)

    for p in people:
        if p.get("wife"):
            Person.people[p["name"]].wife = Person.people[p["wife"]]

        if p.get("husband"):
            Person.people[p["name"]].husband = Person.people[p["husband"]]

    return persons

