import pickle
from Class_Person import Person

person_4 = Person('Oksana', 44, 'financier')

# Сериализация
f = open('person.pkl', 'wb')
pickle.dump(person_4, f)
f.close()

# Десериализация
f = open('person.pkl', 'rb')
person_new = pickle.load(f)

print(person_4)
print(person_new)
f.close()
