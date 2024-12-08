import random

from data.data import Person

from faker import Faker


faker_ru = Faker('ru_RU')
# faker_en = Faker('en_EN')
Faker.seed()



def generated_person():
    yield Person(
        full_name = faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name = faker_ru.first_name(),
        last_name = faker_ru.last_name(),
        age = random.randint(18, 70),
        salary = random.randint(1000, 10000),
        department = faker_ru.job(),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address()

    )

# def generated_person():
#     yield Person(
#         full_name = faker_en.first_name() + " " + faker_en.last_name() + " " + faker_en.middle_name(),
#         email = faker_en.email(),
#         current_address = faker_en.address(),
#         permanent_address = faker_en.address()
#     )
#
