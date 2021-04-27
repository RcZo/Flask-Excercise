from .db import db

class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')

class User(db.Document):    
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))

User.register_delete_rule(Movie, 'added_by', db.CASCADE)
