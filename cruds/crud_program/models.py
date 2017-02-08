from backend import db
from . import models
from cruds.crud_courses.models import Courses


class Program(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    abbreviation = db.Column(db.String(10))
    total_hours = db.Column(db.Integer)
    total_credits = db.Column(db.Integer)
    courses = db.relationship('Courses')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'abbreviation': self.abbreviation,
            'total_hours': self.total_hours,
            'total_credits':  self.total_credits,
            'courses': [course.serialize() for course in self.courses]
        }

    def set_fields(self, fields):
        self.name = fields['name']
        self.abbreviation = fields['abbreviation']
        self.total_hours = fields['total_hours']
        self.total_credits = fields['total_credits']