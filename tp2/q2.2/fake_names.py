from faker import Faker

def create_names(amount):

    fake = Faker()
    names = set()

    while len(names) < amount:
        names.add(fake.name())
    
    return names

