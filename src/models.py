from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250), nullable=False)
    home_planet = db.Column(db.Integer, db.ForeignKey('planet.id' ))
   
    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "home planet": self.home_planet,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250), nullable=False)
    terrain = db.Column(db.String(250))
    homeworld_of = db.relationship('Person', backref='homeworld', lazy= 'dynamic')
   
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }
    
c


class Favorite_People(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id_favorites = db.Column(db.Integer,db.ForeignKey('user.id'))
    favorite_people = db. relationship( 'Person', backref='favorite_people', lazy=' dynamic')

    def serialize(self):
        return {
            "id": self.id,
            "user_id_favorites": self.user
       }

class Favorite_Planets(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id_favorites = db.Column(db.Integer,db.ForeignKey('user.id'))
    favorite_planets = db.relationship( 'Person', backref='favorite_people', lazy=' dynamic')

    def serialize(self):
        return {
            "id": self.id,
            "user_id_favorites": self.user
       }









class Users (db.Model):
    id = db.Column(db. Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db. String (250), nullable=False)
    password = db.Column(db.String (250), nullable=False)
    favorites_of = db.relationship('Favorites', backref='favorites', lazy='dynamic')

    def __ref__(self):
        return '<User %r>' % self.username

#favorites relationship