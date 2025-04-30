from events_app import db
from sqlalchemy.orm import backref
import enum

class FormEnum(enum.Enum):
    """Helper class to make it easier to use enums with forms."""
    @classmethod
    def choices(cls):
        return [(choice.name, choice) for choice in cls]

    def __str__(self):
        return str(self.value)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    events_attending = db.relationship(
        'Event', secondary="guest_events", back_populates="guests")
    
    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'


class EventType(FormEnum):
    NONE = 'Not Specified'
    PARTY = 'Party'
    WEDDING = 'Wedding'
    BIRTHDAY = 'Birthday'
    NETWORKING = 'Networking'
    CONFERENCE = 'Conference'
    JOB = 'Job Fair'
    

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.Enum(EventType), default=EventType.NONE)
    guests = db.relationship(
        'Guest', secondary="guest_events", back_populates="events_attending")

    
    def __str__(self):
        return f'{self.title}'
    
    def __repr__(self):
        return f'{self.title}'
    

guest_event_table = db.Table('guest_events',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
)

