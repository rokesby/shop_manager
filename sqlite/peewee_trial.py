# from peewee import SqliteDatabase
# Useful searches - https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
# Query examples - https://docs.peewee-orm.com/en/latest/peewee/query_examples.html



from peewee import *
from datetime import date


db = SqliteDatabase('sqlite/sql.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


db.create_tables([Person])
db.create_tables([Pet])

Person.truncate_table()
Pet.truncate_table()

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database

uncle_rez = Person(name='Reza', birthday=date(1973, 10, 18))
uncle_rez.save()

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))

herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database.
# Returns: 1


# Add child records
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance() # he had a great life
# Returns: 1

print("All people in the DB")
for person in Person.select():
    print(person.name)

# prints:
# Bob
# Grandma L.
# Herb

print("Cats and their owners")
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

# prints:
# Kitty Bob
# Mittens Jr Herb

print("More efficient than above ( 1 query and not 2)")
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)


print("All of Bob's pets") 
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

# prints:
# Bob
#   * Kitty
#   * Fido
# Grandma L.
# Herb
#   * Mittens Jr
query = Person.select().order_by(Person.name).prefetch(Pet)
for person in query:
    print(person.name)
    for pet in person.pets:
        print('  *', pet.name)

db.close()