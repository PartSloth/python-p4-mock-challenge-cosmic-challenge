from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Planet(db.Model, SerializerMixin):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    distance_from_earth = db.Column(db.Integer)
    nearest_star = db.Column(db.String)

    missions = db.relationship('Mission', back_populates='planet', cascade='all, delete-orphan')

    serialize_rules = ('-missions.planet',)

class Scientist(db.Model, SerializerMixin):
    __tablename__ = 'scientists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    field_of_study = db.Column(db.String)

    missions = db.relationship('Mission', back_populates='scientist', cascade='all, delete-orphan')

    serialize_rules = ('-missions.scientist',)

    @validates('name', 'field_of_study')
    def validate_name_and_study(self, key, value):
        if not value or not value.strip():
            raise ValueError("Scientist must have a name and a field of study.")
        else:
            return value


class Mission(db.Model, SerializerMixin):
    __tablename__ = 'missions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    scientist_id = db.Column(db.Integer, db.ForeignKey('scientists.id'))

    planet = db.relationship('Planet', back_populates='missions')
    scientist = db.relationship('Scientist', back_populates='missions')

    serialize_rules = ('-planet.missions', '-scientist.missions')

    @validates('name', 'scientist_id', 'planet_id')
    def validate_name_and_ids(self, key, value):
        if value:
            return value
        else:
            raise ValueError("Mission must have a name, scientist's id, and planet's id.")


# add any models you may need.
