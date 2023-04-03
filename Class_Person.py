class Person():
    def __init__(self, name, age, post):
        self.name = name
        self.age = age
        self.post = post

    def __str__(self):
        return f'Worker: name-{self.name}, age-{self.age}, post-{self.post}.'

    def __del__(self):
        del self.name
        del self.age
        del self.post

    def id_worker(self):
        return self.name[0] + self.name[-1] + str(self.age) + self.post[0] + self.post[-1]

    def __getitem__(self, item):
        tmp_dict = [self.name, self.age, self.post]
        return tmp_dict[item]

    def __eq__(self, other):
        return (self.name == other.name) & (self.age == other.age) & (self.post == other.post)

    def __lt__(self, other):
        if self.age < other.age:
            return f'{self.name} is younger than {other.name}'
        elif self.age == other.age:
            return f'{self.name} age is equal to {other.name} age'
        else:
            return f'{self.name} is older than {other.name}'

    def __add__(self, other):
        if isinstance(other, str):
            return Person(self.name, self.age, self.post + ' and ' + other)

    def __int__(self):
        return len(self.name) + self.age + len(self.post)

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__ = state


if __name__ == '__main__':

    person_1 = Person('Ivan', 25, 'manager')
    person_2 = Person('Inna', 40, 'director')
    person_3 = Person('Inna', 40, 'director')

    print(person_1)
    print(person_1.id_worker(), person_2.id_worker())

    for item in person_1:
        print(item)

    print(person_1 == person_2)
    print(person_2 == person_3)

    print(person_1 < person_2)
    print(person_2 < person_3)

    print(person_1 + 'consultant')

    print(int(person_1))
