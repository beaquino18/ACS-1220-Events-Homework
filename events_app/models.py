from events_app import db
from sqlalchemy.orm import backref
import enum

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

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

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

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
    date_and_time = db.Column(db.Date, nullable=False)
    guests = db.relationship(
        'Guest', secondary="guest_events", back_populates="events")
    category = db.Column(db.Enum(EventType), default=EventType.NONE)
    
    def __str__(self):
        return f'{self.title}'
    
    def __repr__(self):
        return f'{self.title}'
    

guest_event_table = db.Table('guest_events',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
)

