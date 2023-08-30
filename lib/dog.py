from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
engine = create_engine('sqlite:///:memory:')

def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name == name).first()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session,dog, breed):
   session.query(Dog).filter(Dog.name == dog.name).update({
        Dog.breed: breed
    })