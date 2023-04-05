class Person:
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

    @staticmethod
    def stat_method_ex(name):
        if name == person_1.name:
            return 1
        return 0

    @classmethod
    def class_method_ex(cls):
        name_list = ['Dima', 'Petya', 'Andrey', 'Slava', 'Kseniya', 'Diana', 'Nastya', 'Tolya', 'Sonya', 'Ura']
        age_list = [23, 30, 32, 40, 43, 37, 34, 25, 39, 28]
        post_list = ['manager', 'financier', 'consultant', 'director', 'general engineer', 'developer',
                     'security guard', 'accountant', 'linguist', 'clerk']
        person_list = []
        for i in range(10):
            person_list.append(cls(name_list[i], age_list[i], post_list[i]))
        return person_list


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

    list_ex = Person.class_method_ex()
    print(list_ex)

    for i in range(10):
        print(list_ex[i])

    print(Person.stat_method_ex('Ivan'))